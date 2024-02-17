import  cv2 , time , numpy
from ppadb.client import Client as ADB

adbc = ADB(host='127.0.0.1', port=5037)
devices = adbc.devices()
if len(devices) == 0:
    print('No device attached')
    quit()
device = devices[0]
def save():
    screen_short = device.screencap()
    with open('Screen.png','wb') as f:
        f.write(screen_short)
        time.sleep(.5)
target_list = ['rx.png','ry.png','gx.png','gy.png','bx.png','by.png','yx.png','px.png','py.png','st.png']
tem_plate = cv2.imread('Screen.png')
def tread(color):
    target_name = cv2.imread(color)
    tem_plate = cv2.imread('Screen.png')
    try:result = cv2.matchTemplate(tem_plate,target_name,cv2.TM_SQDIFF_NORMED)
    except:
        print('Not result')
        return
    else:
        log_cut = numpy.where(result<=0.05)
        log_complate = list(zip(*log_cut[::-1]))
        for loc in log_complate:
            device.shell(f'input tap {loc[0]+5} {loc[1]+5}')
            device.shell(f'input tap {loc[0]+5} {loc[1]+5}')
            print('click',color)
            cv2.waitKey(1)
            save()
            return
while True:
    save()
    tread(target_list[0])
    tread(target_list[1])
    tread(target_list[2])
    tread(target_list[3])
    tread(target_list[4])
    tread(target_list[5])
    tread(target_list[6])
    tread(target_list[7])
    tread(target_list[8])
    tread(target_list[9])


