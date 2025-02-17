import cv2 as cv
vid = cv.VideoCapture(0)


while(True):
    ret, frame = vid.read()
    cv.imshow('frame', frame)
    imgray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    thresh3 = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,  115, 1)
    cv.imshow('new', thresh3)
    cv.imshow("newonw", imgray)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
    

vid.release()
cv.destroyAllWindows()
