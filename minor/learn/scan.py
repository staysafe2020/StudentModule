
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap=cv2.VideoCapture(0)

while True:
 aaa=''
 _,frame=cap.read()
 decodeObjects=pyzbar.decode(frame)
 for obj in decodeObjects:
  #print("Data:",obj.data)
  aaa=obj.data
  points=obj.polygon
  
 
  if len(points) > 4: 
    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
    hull = list(map(tuple, np.squeeze(hull)))
  else: 
    hull = points;
  
  
  n = len(hull)     
        # Draw the convext hull
  for j in range(0,n):
    cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

    #x = decodedObject.rect.left
    #y = decodedObject.rect.top


  




 cv2.imshow("Frame",frame)
 key=cv2.waitKey(1)
 if(key==27):
  break
 if(len(aaa)>0 and aaa!=''):
  aaa=str(aaa)
  data=aaa[2:len(aaa)-1]
  data=data.split(" ")
  
  break


cap.release()
cv2.destroyAllWindows()

@staticmethod
def Hello():
 return 'Hello World'