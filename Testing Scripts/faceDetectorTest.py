import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

  
cap = cv2.VideoCapture(0)

   
detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

   
while True:
       
    success, img = cap.read()

       
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
           
        for bbox in bboxs:
                
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)

            
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
            cvzone.putTextRect(img, f'{score}%', (x, y - 10))
            cvzone.cornerRect(img, (x, y, w, h))

        
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()