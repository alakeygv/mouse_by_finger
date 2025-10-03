from cvzone.HandTrackingModule import HandDetector
import autopy
import cv2, time

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)
pTime = cTime = 0
width, height = autopy.screen.size()

def smart_round(number, precision=2.5):
    if number % precision == 0:
        return number
    return precision * round(number / precision)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    hands, img = detector.findHands(img, draw=True)  
    
    #if hands:
        #print(hands[0]["lmList"][8])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    try:
        x_Mouse = hands[0]["lmList"][8][0]
        y_Mouse = hands[0]["lmList"][8][1]
        
        #cv2.circle(img, (hands[0]["lmList"][8][0], hands[0]["lmList"][8][1]), 10, (255, 0, 0), cv2.FILLED)

        autopy.mouse.move(smart_round(x_Mouse * width / w), smart_round(y_Mouse * height / h))
        
        if abs(hands[0]["lmList"][11][0] - hands[0]["lmList"][4][0]) < 40 and abs(hands[0]["lmList"][11][1] - hands[0]["lmList"][4][1]) < 7 and abs(hands[0]["lmList"][11][2] - hands[0]["lmList"][4][2]) < 11:
             autopy.mouse.click()
        
    except:
        pass

    #cv2.imshow("Image", img)

    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
