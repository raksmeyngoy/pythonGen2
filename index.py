import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    parking_slots = {"free": 0,
                     "occupied": 0}

    for box in results.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        conf = box.conf[0]
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if label == "car":
            parking_slots["occupied"] += 1
            color = (0, 0, 255)
        else:
            parking_slots["free"] += 1
            color = (0, 255, 0)

        cv2.rectangle(frame, (x1, y1),
                      (x2, y2), color, 2)
        cv2.putText(frame, label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    color, 2)

    total = parking_slots["free"] + parking_slots["occupied"]
    cv2.putText(frame, f"Free: {parking_slots['free']} / "
                       f"Occupied: {parking_slots['occupied']}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Parking Slots", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()