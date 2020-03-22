import cv2
import argparse


def get_args():
    parser = argparse.ArgumentParser("Background Subtraction")
    i_desc = "The location of video input, default is stock.mkv"
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-i", help=i_desc, default=0)
    args = parser.parse_args()
    return args

args = get_args()
subBack = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture(args.i, apiPreference = cv2.CAP_ANY )
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

        
    
