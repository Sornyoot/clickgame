from kivy.app import App
import  cv2 , time , numpy
from ppadb.client import Client
from kivy.core.window import Window
Window.size = (50,50)

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]
class Myapp(App):
    def build(self):
        screen_short = device.screencap()
        with open('Screen.png','wb') as f:
            f.write(screen_short)
            device.shell(f'input tap 500 450')
            device.shell(f'input tap 500 450')
            time.sleep(.5)
        return
if __name__ == "__main__":
 Myapp().run()