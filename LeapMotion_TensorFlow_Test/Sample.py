################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

import pyautogui

import time

import re

file_out = open("newdata.csv", 'a')


# TENSORFLOW
import tensorflow as tf

import numpy as np
import random
import pandas as pd


screenWidth = pyautogui.size()[0]
screenHeight = pyautogui.size()[1]
print(screenWidth)
print(screenHeight)

mouseX = screenWidth/2
mouseY = screenHeight/2


mouseSpeed = 20



# TRAINING = "leapMotionTrainingSet.csv"
# TEST = "leapMotionTestSet.csv"

# dataset = pd.read_csv("newdata.csv")
# dataset['n'] = dataset['n'].astype('int')

# dfLength = len(dataset)

# trainingLength = int(0.8 * dfLength)
# testLength = int(0.2 * dfLength)

# trainingSetRandomRows = np.random.choice(dataset.index.values, trainingLength)
# trainingData = dataset.iloc[trainingSetRandomRows]
# trainingData.to_csv(TRAINING, index=False, header=False)

# testSetRandomRows = np.random.choice(dataset.index.values, testLength)
# testData = dataset.iloc[testSetRandomRows]
# testData.to_csv(TEST, index=False, header=False)

# trainingSet = tf.contrib.learn.datasets.base.load_csv_without_header(
#     filename=TRAINING, target_dtype=np.int, features_dtype=np.float32
# )

# testSet = tf.contrib.learn.datasets.base.load_csv_without_header(
#     filename=TEST, target_dtype=np.int, features_dtype=np.float32
# )

# featureColumns = [tf.contrib.layers.real_valued_column("", dimension=13)]

# classifier = tf.contrib.learn.DNNClassifier(
#                 n_classes=2,
#                 feature_columns=featureColumns,
#                 hidden_units=[20, 30, 20]
# )

# # Fit model
# classifier.fit(
#                 x=trainingSet.data,
#                 y=trainingSet.target,
#                 batch_size=128,
#                 steps=2000)

# predictions = classifier.predict(np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1]]))

# print 'Predictions: ', list(predictions)




class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']


    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #       frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands

        predictIn = []
        predictIn.append([])
        
        global mouseX
        global mouseY
        global screenWidth
        global screenHeight
        global mouseSpeed

        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            # print "  %s, id %d, position: %s" % (
            #     handType, hand.id, hand.palm_position)


            if(hand.is_left):
                file_out.write("0,")
                predictIn[0].append(float(0))
            else:
                file_out.write("1,")
                predictIn[0].append(float(1))



            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #     direction.yaw * Leap.RAD_TO_DEG)



            # FILE OUT
            file_out.write("{0},{1},{2},".format(direction.pitch, normal.roll, direction.yaw))

            predictIn[0].append(float(direction.pitch))
            predictIn[0].append(float(normal.roll))
            predictIn[0].append(float(direction.yaw))


            # Get arm bone
            arm = hand.arm
            # print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
            #     arm.direction,
            #     arm.wrist_position,
            #     arm.elbow_position)



            # FILE OUT
            # ARM DIRECTION
            arm_dir_str = re.sub("[^0-9^.^-]", " ", str(arm.direction))
            arm_dir_vals = arm_dir_str.split()

            for val in arm_dir_vals:
                file_out.write(val + ",")
                predictIn[0].append(float(val))


            # WRIST POSITION
            wrist_pos_str = re.sub("[^0-9^.^-]", " ", str(arm.wrist_position))
            wrist_pos_vals = wrist_pos_str.split()

            for val in wrist_pos_vals:
                file_out.write(val + ",")
                predictIn[0].append(float(val))          


            x_min = -220
            x_max = 150
            y_min = 400
            y_max = 50

            a_x = 0
            b_x = 2048
            a_y = 0
            b_y = 1152

            x = int(float(wrist_pos_vals[0]))
            y = int(float(wrist_pos_vals[1]))

            mouseX = a_x + (x - x_min) * (b_x - a_x) / (x_max - x_min)
            mouseY = a_y + (y - y_min) * (b_y - a_y) / (y_max - y_min)

            print mouseX
            print mouseY

            if(hand.is_left):
                pyautogui.moveTo(mouseX, mouseY, 0.1, pyautogui.easeOutQuad)


            # ELBOW POSITION
            elbow_pos_str = re.sub("[^0-9^.^-]", " ", str(arm.elbow_position))
            elbow_pos_vals = elbow_pos_str.split()

            for val in elbow_pos_vals:
                file_out.write(val + ",")
                predictIn[0].append(float(val))



            # Get fingers
            for finger in hand.fingers:

                # print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                #     self.finger_names[finger.type],
                #     finger.id,
                #     finger.length,
                #     finger.width)

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    # print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                    #     self.bone_names[bone.type],
                    #     bone.prev_joint,
                    #     bone.next_joint,
                    #     bone.direction)

                    # EXTRACT BONE START POSITIONS    
                    bone_start_vals_str = re.sub("[^0-9^.^-]", " ", str(bone.prev_joint))
                    bone_start_vals = bone_start_vals_str.split()

                    #for val in bone_start_vals:
                        #file_out.write(val + ",")


                    # EXTRACT BONE END POSITIONS  
                    bone_end_vals_str = re.sub("[^0-9^.^-]", " ", str(bone.next_joint))
                    bone_end_vals = bone_end_vals_str.split()

                    #for val in bone_end_vals:
                        #file_out.write(val + ",")


                    # EXTRACT BONE DIRECTION
                    bone_direction_vals_str = re.sub("[^0-9^.^-]", " ", str(bone.direction))
                    bone_direction_vals = bone_direction_vals_str.split()

                    #for val in bone_direction_vals:
                        #file_out.write(val + ",")

            # Get gestures
            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    circle = CircleGesture(gesture)

                    # Determine clock direction using the angle between the pointable and the circle normal
                    if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                        clockwiseness = "clockwise"
                        pyautogui.scroll(-4)
                    else:
                        clockwiseness = "counterclockwise"
                        pyautogui.scroll(4)

                    # Calculate the angle swept since the last frame
                    swept_angle = 0
                    if circle.state != Leap.Gesture.STATE_START:
                        previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                        swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI


                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    swipe = SwipeGesture(gesture)
                    pyautogui.hotkey('alt', 'left')


                if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                    keytap = KeyTapGesture(gesture)
                    #pyautogui.click(button='right')
                    pyautogui.click()
                    print "CLICK"

                if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                    screentap = ScreenTapGesture(gesture)
                    pyautogui.click()
                    print "CLICK"



            # print predictIn

            # predictionsList = list(classifier.predict(np.array(predictIn)))
            # print 'Predictions: ', predictionsList[0]


            # if predictionsList[0] == 0:
            #     print 'ctrl -'
            #     pyautogui.hotkey('ctrl', '-')
            
            # if predictionsList[0] == 1:
            #     print 'ctrl +'
            #     pyautogui.hotkey('ctrl', '+')

            # if predictionsList[0] == 2:
            #     mouseX -= mouseSpeed

            # if predictionsList[0] == 3:
            #     mouseX += mouseSpeed



            # print mouseX
            # print " "
            # print mouseY

            # pyautogui.moveTo(mouseX, mouseY)

            # file_out.write(str(1))

            # file_out.write("\n")

            print "\n"

            # time.sleep(1)


    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
