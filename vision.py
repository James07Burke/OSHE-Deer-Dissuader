import cv2
import time
from ultralytics import YOLO

# Loading custom yolo model
yolo = YOLO('/home/redrileyp/DeerDissuader/runs/detect/yolov8_deerdetector/weights/best.pt')

# Opening video feed
videoCap = cv2.VideoCapture('/home/redrileyp/DeerDissuader/deer.mp4')

# Function to get class colors
def getColors(cls_num):
    base_colors = [(255,0,0), (0,255,0), (0,0,255)]
    color_index = cls_num % len(base_colors)
    increments = [(1,-2,1),(-2,1,-1), (1,-1,2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)

frame_width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = videoCap.read()
    if not ret:
        continue

    # Processing frame to RGB for yolo
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = yolo.predict(rgb_frame, conf = 0.4) # Confidence prediction is 70%

    for result in results:
        classes_names = result.names
        for box in result.boxes:
            deerSeen = False
            # Check if confidence is greater than 75%
            if box.conf[0] > 0.5:
                # Get coords
                [x1,y1,x2,y2] = box.xyxy[0]
                # Convert to int
                x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
                # Get class
                cls = int(box.cls[0])
                # Get class name
                class_name = classes_names[cls]
                # Get class color
                color = getColors(cls)
                # Draw rectangle
                cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
                # Apply class name and confidence on image
                cv2.putText(frame, f'{classes_names[int(box.cls[0])]}{box.conf[0]:.2f}', (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
                # Deer seen variable for sound triggering and video capture
                deerSeen = True
                out.write(frame)
        
        # Show the final image
        cv2.imshow('frame',frame)
        
        # Break loop is 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up
out.release()
videoCap.release()
cv2.destroyAllWindows()
        