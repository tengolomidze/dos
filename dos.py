from matplotlib.pyplot import get
import requests, threading, time;

REQUESTS =128;
THREADS = 128;

def Start():
    for i in range(0, THREADS):
        newThread = threading.Thread(target=Get, args=[i])
        newThread.start()

def Get(i):
    for j in range(0, REQUESTS):
        try:
            r = requests.get("https://geomc.ge/")
            print(r)
        except:
            print("Falied.")
    
Start()
