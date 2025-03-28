from ultralytics import YOLO

# Load a pre-trained YOLOv11 model
model = YOLO('yolov8s.yaml')  # Use 'yolov11n.pt' for the nano version

# Train the model
model.train(
    data='/home/redrileyp/DeerDissuader/data.yaml',  # Path to data.yaml
    epochs=200,
    imgsz=640,
    batch=64,
    name='yolov8_deer',
    device=0  # Set to 'cpu' if GPU is not available
)

