import  cv2 , time , numpy
from ppadb.client import Client as adbc

client = adbc(host='127.0.0.1', port=5037)
decives = client.devices()
decive = decives[0]


def save():
    screenshort = decive.screencap()
    with open('Screen.png', 'wb') as f:
        f.write(screenshort)
        time.sleep(.5)

save()
