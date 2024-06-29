from ultralytics import YOLO
 
model = YOLO('yolov8x')

model.predict('input_files/input_video.mp4', save  = True)