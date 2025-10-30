import os
import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    # カメラを起動してユーザが'q'を押すまで待ち、最後のフレームを取得する
    app.run()

    # メモリ上のキャプチャ画像を取得（ファイル保存機能は使わない）
    capture_img = app.get_img()
    if capture_img is None:
        print("カメラ画像が取得できませんでした。run()で'q'を押してキャプチャしてください。")
        return

    # 置き換え対象のGoogle画像を読み込む
    google_img = cv2.imread('images/google.png')
    if google_img is None:
        print("images/google.png が見つかりません。ファイルパスを確認してください。")
        return

    # 画像サイズを取得
    g_hight, g_width = google_img.shape[:2]
    c_hight, c_width = capture_img.shape[:2]
    print(f"google: {g_width}x{g_hight}, camera: {c_width}x{c_hight}")

    # (0,0)からグリッド状にキャプチャ画像を並べ、白色ピクセルのみ置き換える
    for y in range(g_hight):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                tile_x = x // c_width
                tile_y = y // c_hight
                local_x = x - tile_x * c_width
                local_y = y - tile_y * c_hight

                # キャプチャ画像の領域に含まれる場合のみ置き換える（途中で切れるのは許容）
                if 0 <= local_x < c_width and 0 <= local_y < c_hight:
                    google_img[y, x] = capture_img[local_y, local_x]

    # 結果を output_images フォルダに保存
    os.makedirs('output_images', exist_ok=True)
    out_path = 'output_images/lecture05_01_K24097.png'
    cv2.imwrite(out_path, google_img)
    print(f"保存しました: {out_path}")