import cv2

vid = 'stock.mkv'
subBack = cv2.createBackgroundSubtractorMOG2()

capture = cv2.VideoCapture(vid, apiPreference = cv2.CAP_ANY )
if capture.isOpened:
    while True:
        keyboard = cv2.waitKey(20)
        ret, frame = capture.read()
        if frame is None:
            break
        mask = subBack.apply(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        if keyboard == 'q' or keyboard == 27:
            break

        
    
