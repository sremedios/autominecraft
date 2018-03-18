import time
import os
import sys
import numpy as np
import csv
import copy
from win32api import GetCursorPos
from utils import capture_inputs, capture_screen
from utils.VirtualKeyCodesLookUp import keycode2description as k2d
from collections import OrderedDict

if __name__ == '__main__':

    ########## GET ALL DESCRIPTIONS OF KEYCODES ##########

    k2d = OrderedDict(sorted(k2d.items()))

    all_descriptions = []
    all_descriptions.append("time")

    for code, description in k2d.items():
        all_descriptions.append(description)

    all_descriptions.append("mouseX")
    all_descriptions.append("mouseY")
    all_descriptions.append("scrollForward")
    all_descriptions.append("scrollBackward")

    ########## DIRECTORIES & MISC ##########

    TRAIN_DIR = os.path.join("data", "train")
    IMG_DIR = os.path.join(TRAIN_DIR, "images")
    INPUTS_DIR = os.path.join(TRAIN_DIR, "inputs")

    for d in [TRAIN_DIR, IMG_DIR, INPUTS_DIR]:
        if not os.path.exists(d):
            os.makedirs(d)

    inputs_file = os.path.join(INPUTS_DIR, "inputs.csv")

    # initialize csv data file 
    if not os.path.exists(inputs_file):
        with open(inputs_file, 'w') as csvfile:
            fieldnames = all_descriptions
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


    ########## LOOP ##########

    
    while(True):
        # get current time in milliseconds
        now = str(round(time.time()*1000))
        cur_inputs = {}

        # get screen at this time
        capture_screen.screenGrab(time=now, dst_dir=IMG_DIR)

        # get inputs at this time
        for code, description in k2d.items():
            cur_inputs[description] = capture_inputs.key_down(code)

        # get mouse location at this time
        mouse_X, mouse_Y = GetCursorPos()

        # get scrollwheel data
        #scrollF = capture_inputs.scroll_wheel_forward(mouse_X, mouse_Y)
        #scrollB = capture_inputs.scroll_wheel_backward(mouse_X, mouse_Y)
        scrollF = scrollB = 0 # temporary

        cur_inputs["mouseX"] = mouse_X
        cur_inputs["mouseY"] = mouse_Y
        cur_inputs["time"] = now
        cur_inputs["scrollForward"] = scrollF
        cur_inputs["scrollBackward"] = scrollB

        # write results to file
        with open(inputs_file, 'a') as csvfile:
            fieldnames = all_descriptions
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(cur_inputs)
        
        # sleep 1/60 seconds for 60fps capture
        time.sleep(1./60)
