import RPi.GPIO as GPIO
import cv2
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
cap = cv2.VideoCapture(0)

try:
    while True:
        _in = input()
        if _in == '':
            GPIO.output(13, GPIO.HIGH)
            ret, frame = cap.read()
            GPIO.output(13, GPIO.LOW)
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            cv2.imwrite(f'/home/pi/{int(ts)}.png', frame)
except Exception as e:
    print(e)
