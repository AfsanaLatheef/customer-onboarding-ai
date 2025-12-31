from ultralytics import YOLO

# Train
model = YOLO('yolov8n.pt')
model.train(
    data='data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    fliplr=0,          # no flip for IDs
    name='id_detect_5'
)

print("Training finished! Best model → runs/detect/id_detect_5/weights/best.pt")
