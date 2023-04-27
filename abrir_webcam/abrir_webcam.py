import cv2 # pip install opencv-python # pip install opencv-contrib-python

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # caso demore para abrir sua camera, teste esse

if not cap.isOpened():
    print("nao abriu")
    exit()

windowName = "Imagem Mil Grau"

while True:
    ret, frame = cap.read()

    if not ret:
        print("nao tem frame")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.putText(frame, "Inteligencia Mil Grau", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    frame = cv2.circle(frame, (100,100), 40, (255,0,0), 3)

    cv2.imshow(windowName, frame)

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

    if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()
cap.release()
print("Encerrou")
