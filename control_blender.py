import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

video=cv2.VideoCapture(0)
startDist=None
scale=0
detector=HandDetector(detectionCon=0.5)
while True:
    ret,frame=video.read()
    hands,img=detector.findHands(frame)
    if len(hands)==2:
        if(detector.fingersUp(hands[0])==[1,1,0,0,0] and detector.fingersUp(hands[1])==[1,1,0,0,0]):
            if startDist is None:
                length,info,img=detector.findDistance(hands[0]["center"],hands[1]["center"],img)
                startDist=length
            length,info,img=detector.findDistance(hands[0]["center"],hands[1]["center"],img)
            scale=int((length-startDist)//2)
            print(scale)
    else:
        startDist=None
        scale=0
    try:
        pyautogui.scroll(scale)
    except:
        pass
    cv2.imshow("Frame",frame)
    k = cv2.waitKey(1)
    if k==ord("q"):
        break

