import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    # カメラの画像を読み込む
    _, frame = cap.read()
    # 画像を縮小表示する
    frame = cv2.resize(frame, (500, 300))
    # ウィンドウに画像を出力
    cv2.imshow('OpenCV Web Camera', frame)
    k = cv2.waitKey(1)
    if k == 27 or k == 23: break

cap.release()
cv2.destroyAllWindows # ウィンドウを破棄