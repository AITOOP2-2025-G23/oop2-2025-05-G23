import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # --- カメラキャプチャ実行 ---
    app = MyVideoCapture()
    app.run()

    # --- 元画像とキャプチャ画像を取得 ---
    google_img: cv2.Mat = cv2.imread('images/google.png')
    # capture_img は MyVideoCapture の中で取得されたフレームを利用
    capture_img: cv2.Mat = app.get_img()   # ← get_img関数を使う（保存機能は使わない）

    # --- 画像サイズを確認 ---
    g_h, g_w, g_c = google_img.shape
    c_h, c_w, c_c = capture_img.shape
    print(f"google_img: {google_img.shape}")
    print(f"capture_img: {capture_img.shape}")

    # --- キャプチャ画像をグリッド状に敷き詰めるための処理 ---
    # 出力画像をコピーして編集
    result_img = google_img.copy()

    for y in range(g_h):
        for x in range(g_w):
            b, g, r = google_img[y, x]
            # 白色部分を置換
            if (b, g, r) == (255, 255, 255):
                # キャプチャ画像上の座標を繰り返し使う
                yy = y % c_h
                xx = x % c_w
                result_img[y, x] = capture_img[yy, xx]

    # --- 書き込み処理 ---
    cv2.imwrite("lecture05_01_K24037.png", result_img)
    print("lecture05_01_K24037.png を保存しました。")