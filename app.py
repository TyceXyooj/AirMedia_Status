import os
import csv
import time
import threading
from flask import Flask, render_template, jsonify
from flaskwebgui import FlaskUI
from AirMedia import AirMedia

app = Flask(__name__)

airmedias = []
device_statuses = {}  # Stores the latest status for each IP
status_lock = threading.Lock()

# --- LOAD DEVICES ON STARTUP ---
csv_path = os.path.join('static', 'devices.csv')
if os.path.exists(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0 and (row[0].lower() == 'name' or not row[1].replace('.', '').isdigit()):
                continue
            if len(row) >= 2:
                name = row[0].strip()
                ip = row[1].strip()
                airmedias.append(AirMedia(ip, name))


# --- BACKGROUND WORKER (Pings in batches of 10 safely) ---
def background_status_checker():
    while True:
        batch_size = 10
        for i in range(0, len(airmedias), batch_size):
            batch = airmedias[i:i + batch_size]
            
            # Ping this small batch
            for device in batch:
                status = device.getStatus()
                with status_lock:
                    device_statuses[device.getIP()] = status
            
            # Pause 0.5 seconds between batches so network security doesn't flag it
            time.sleep(0.5)
            
        # Wait 30 seconds before running the next full cycle
        time.sleep(30)

# Start the background worker thread when Flask boots up
t = threading.Thread(target=background_status_checker, daemon=True)
t.start()


@app.route("/")
def home():
    return render_template('index.html')


# Instantly returns cached statuses (No timeout, no network blocking!)
@app.route('/updatestatus')
def update():
    status_results = []
    with status_lock:
        for device in airmedias:
            status_results.append({
                "name": device.getName(),
                "ip": device.getIP(),
                "online": device_statuses.get(device.getIP(), False)
            })
    return jsonify(status_results)


if __name__ == "__main__":
    FlaskUI(app=app, server="flask", width=800, height=600).run()