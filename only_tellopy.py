import time
import cv2
from djitellopy import Tello

# グローバル変数として座標を初期化
i, j = 0, 0

# ドローンを初期化
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
    if key == ord('l'):
        return 'land'
    return 'stop'

while True:
    key = getKeyboardInput()
    global i, j

    if key == 'q':
        break
    elif key == 'right' and i < 4:
        tello.move_right(50)
        i += 1
    elif key == 'left' and i > 0:
        tello.move_left(50)
        i -= 1
    elif key == 'up' and j < 4:
        tello.move_up(50)
        j += 1
    elif key == 'down' and j > 0:
        tello.move_down(50)
        j -= 1
    elif key == 'land':
        tello.land()
        break

    print(f"Current position: i={i}, j={j}")

print("終了")
