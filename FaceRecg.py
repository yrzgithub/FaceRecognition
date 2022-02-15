import face_recognition
import cv2
from keyboard import is_pressed

name = input("Enter your name: ")
camera = cv2.VideoCapture(0)

while not is_pressed("esc"):
    _, img = camera.read()
    if not _:
        continue
    locations = face_recognition.face_locations(img)
    if len(locations) != 1:
        continue
    (a, b, c, d) = locations[0]
    cv2.rectangle(img, (d, a), (b, c), thickness=2, color=(0, 255, 0))
    img = cv2.putText(img, text=name, color=(0, 255, 0), thickness=2, org=(d+50, c+30), fontScale=1,
                      fontFace=cv2.FONT_ITALIC)
    cv2.imshow("name", img)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
