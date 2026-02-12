import cv2
import sys
from os import path
from pathlib import Path

detector_model = path.join(Path(__file__).resolve().parent, "models/face_detection.onnx")

if not path.exists(detector_model):
    print(f"找不到模型檔案：{detector_model}")
    sys.exit(1)

try:
    face_detector = cv2.FaceDetectorYN.create(
        detector_model,              # model
        "",                          # config, YuNet 不需要額外的 config 檔
        (640, 480),                  # input_size, 模型運算的輸入尺寸
        0.5,                         # score_threshold, 高於此值的置信度偵測結果才會保留
        0.3,                         # nms_threshold, 此值用於非極大值抑制 (NMS)，當兩個偵測框的重疊度超過此值時，會保留置信度較高的框   
        5000,                        # top_k, 在 NMS 後保留的最大偵測框數量
        cv2.dnn.DNN_BACKEND_DEFAULT, # backendId, 使用 OpenCV 預設的 DNN 後端
        cv2.dnn.DNN_TARGET_CPU       # targetId, 使用 CPU 作為運算裝置
    ) 
    
except Exception as e:
    print(f"載入模型時發生錯誤: {e}")
    sys.exit(1)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法開啟攝影機")
    sys.exit(1)

# 取得攝影機畫面的寬高，避免在迴圈中反覆呼叫 shape，提升效能(同 input_size)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
face_detector.setInputSize((frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法取得畫面，退出...")
        break

    # 偵測臉部
    # 注意：FaceDetectorYN.detect 會回傳 (retval, faces)
    _, faces = face_detector.detect(frame) # faces 的格式為 (num_faces, 15)，每一行包含 [x, y, w, h, landmark1_x, landmark1_y, ..., landmark5_x, landmark5_y, confidence]

    # 確保 faces 有內容
    if faces is not None:
        for face in faces:
            # 臉部外框
            box = face[0:4].astype(int)
            cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (255, 0, 0), 2)

            # 五官特徵點 (Landmarks)
            landmarks = face[4:14].reshape(5, 2).astype(int)
            for landmark in landmarks:
                cv2.circle(frame, (landmark[0], landmark[1]), 2, (0, 255, 0), -1)
            
            # 置信度 (Confidence)
            confidence = face[14]
            cv2.putText(frame, f"{confidence:.2f}", 
                        (box[0], box[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow('Face Detection (YuNet)', frame)
    
    # 按下 ESC (27) 退出
    if cv2.waitKey(1) == 27:
        print("使用者結束程式")
        break

cap.release()
cv2.destroyAllWindows()