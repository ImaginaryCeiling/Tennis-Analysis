from ultralytics import YOLO
 
model = YOLO('yolov516u.pt')

model.predict('input_files/image.png', save  = True)