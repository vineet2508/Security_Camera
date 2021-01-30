import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff=cv2.absdiff(frame1, frame2)
    grey = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    _, thresh=cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    cont, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, cont, -1, (0, 255, 0), 2)
    for c in cont:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #    winsound.Beep(500, 200)
        winsound.PlaySound('Police_Siren.WAV', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Security Camera', frame1)
