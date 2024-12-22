import time
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

def getKeyboardInput():
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        return 'q'
    if key == ord('w'):
        return 'forward'
    if key == ord('s'):
        return 'back'
    if key == ord('a'):
        return 'left'
    if key == ord('d'):
        return 'right'
    if key == ord('u'):
        return 'up'
    if key == ord('j'):
        return 'down'
    if key == ord('i'):
        return 'cw'
        # 時計回りに回転
    if key == ord('k'):
        return 'ccw'
        # 反時計回りに回転
    if key == ord('l'):
        return 'land'
    return 'stop'

while True:
    key = getKeyboardInput()
    if key == 'q':
        break
    elif key == 'forward':
        tello.move_forward(30)
    elif key == 'back':
        tello.move_back(30)
    elif key == 'left':
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == 'up':
        tello.move_up(30)
    elif key == 'down':
        tello.move_down(30)
    elif key == 'cw':
        tello.rotate_clockwise(30)
    elif key == 'ccw':
        tello.rotate_counter_clockwise(30)
    elif key == 'land':
        tello.land()
        break

print("終了")