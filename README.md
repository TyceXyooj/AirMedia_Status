# AirMedia Monitor

Monitor the online status of Crestron AirMedia devices (and other network endpoints) from a lightweight desktop window.

## Overview

AirMedia Monitor takes a list of device names and IP addresses on your local network and displays their real-time online/offline status in a clean desktop interface. While originally built for tracking Crestron AirMedia presentation receivers, it works with **any network device that responds to ICMP ping requests** (such as printers, displays, switches, or servers).

## Features

* **Real-Time Status Dashboard:** Displays whether configured devices are online or offline in a dedicated desktop window.
* **Universal Ping Support:** Works with Crestron AirMedia units as well as any pingable IPv4 device on your network.
* **Simple CSV Configuration:** Easily add, remove, or rename monitored devices by editing a plain-text CSV file.
* **One-Click Launch:** Includes a Windows batch launcher (`run.bat`) for quick startup without manually typing terminal commands.

## Prerequisites

### System & Network Requirements
* **Operating System:** Windows (required by the current launcher and desktop window configuration).
* **Python:** Python 3.8 or higher installed and added to your Windows `PATH`.
* **Network Access:** The host machine must be able to reach the target IP addresses over ICMP (ping). Ensure target devices are not isolated by VLAN segmentation, firewall rules, or ACLs blocking ping traffic.

### Python Libraries
The project relies on the following core packages:
* `Flask`
* `flaskwebgui`
* `ping3`
* `psutil`

## Installation

1. **Clone or download the repository:**
   ```bash
   git clone [https://github.com/TyceXyooj/AirMedia_Status.git](https://github.com/TyceXyooj/AirMedia_Status.git)
   cd AirMedia_Status
