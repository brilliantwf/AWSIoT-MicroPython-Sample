WIFI_SSID = "Wifi_SSID"
WIFI_PW = "You_Wifi_Password"
from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
def connect_wifi(ssid, pw):
    import machine
    from network import WLAN
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pw)
    while not wlan.isconnected():
        machine.idle()  # save power while waiting
        print('WLAN connection succeeded!')
        break
    print("connected:", wlan.ifconfig())
    led.value(1)
    sleep(1)
    led.value(0)
try:
    print("Connecting WIFI")
    connect_wifi(WIFI_SSID, WIFI_PW)
except Exception as e:
    print(str(e))
