from ping3 import ping, verbose_ping

class AirMedia(object):
    #constructor
    def __init__(self,ip,name):
        if isinstance(ip,str):
            self.__ip = ip
        else:
            print('IP needs to be a string.')
        if isinstance(name,str):
            self.__name = name
        else:
            print('Name needs to be a string.')

    #returns the IP of the device
    def getIP(self):
        return self.__ip

    #return the name of the device
    def getName(self):
        return self.__name

    #returns if the device is online
    def getStatus(self):
        return ping(self.__ip, timeout = 1)