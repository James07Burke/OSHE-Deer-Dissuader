import cv2
from ultralytics import YOLO
import pygame
from datetime import datetime

# Load model and initialize camera
model = YOLO('/path/to/model/best.pt')
cap = cv2.VideoCapture(0)

pygame.mixer.init() # Initialize audio

while True:
    ret, frame = cap.read() # Load frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Formatting frame for easy model detection
    results = model.predict(source=rgb_frame, verbose=False, stream=True, show=True)

    for result in results:
        class_name = result.names
        for box in result.boxes:
            if len(result.boxes.cls) > 0.6 and box.conf[0] > 0.7:
                dclass = result.boxes.cls[0].item()

                # Get coords
                [x1,y1,x2,y2] = box.xyxy[0]
                # Convert to int
                x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
                # Get class
                cls = int(box.cls[0])
                # Get class name
                class_name = class_name[cls]
                # Draw rectangle
                cv2.rectangle(frame, (x1,y1), (x2,y2), 2)
                # Apply class name and confidence on image
                cv2.putText(frame, f'{class_name[int(box.cls[0])]}{box.conf[0]:.2f}', (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 1, 2)

                if dclass==0.0:
                    if pygame.mixer.music.get_busy():   # Keep busy while audio playing
                        print("Audio is playing")
                    else:
                        # Load and play audio
                        pygame.mixer.music.load("/path/to/audio.mp3")
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.music.play()
                        
cap.release()
cv2.destroyAllWindows()
