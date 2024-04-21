######################################
######################################
# Copyright (c) 2024 Di Filippo Davide
######################################
######################################
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import math

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 480)
success, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(detectionCon=0.8, maxHands=1)
sensitivity_max_1 = 3
sensitivity_1_min = 2.2
sensitivity_max_2 = 10
sensitivity_2_min = 9

angle_t_pre = 0.0
angle_2_pre = 0.0


class Angles_yx:

    def __init__(self, part) -> None:
        # Calculate the angle difference
        self.wrist = lmList[0]
        self.point_ang = [part[0], part[1]]    
        self.diff_ang = [self.point_ang[0]- self.wrist[0], self.point_ang[1]-self.wrist[1]]
    
    def calculation(self):
        # Calculate the angle created between the wrist and the various fingers
        self.angle = math.degrees(math.atan2(self.diff_ang[1], self.diff_ang[0]))
        return self.angle*-1


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        bbox = hand["bbox"]

        # Create instances of the Angles class
        
        middle = Angles_yx(lmList[12])
        index = Angles_yx(lmList[8])
        ring = Angles_yx(lmList[16])
        thumb = Angles_yx(lmList[4])
        pinky = Angles_yx(lmList[20])
        
        pinky_under = lmList[18]
        thumb_ = lmList[4]
        wrist_ = lmList[0]
        middle_ = lmList[12]
        index_ = lmList[8]
        ring_ = lmList[16]
        pinky_ = lmList[20]
        
        # Calculates the combined angle between all fingers and wrist and returns the angle

        elements_list = [middle, index, ring, thumb, pinky]
        sum_list = [middle.calculation() + index.calculation() + ring.calculation() + thumb.calculation() + pinky.calculation()]
        angle_sum = sum(sum_list)
        n = len(elements_list)
        angle_t = angle_sum/n

        # Calculates the angle between your finger and the midpoint of your little finger to create a y/z tilt axis
        
        p_thumb = [thumb_[0], thumb_[1], thumb_[2]]
        p_pinky_under = [pinky_under[1], pinky_under[2]]
        p_one_p_t = [p_thumb[1] - p_pinky_under[0], p_thumb[2] - p_pinky_under[1]]     
        angle_2 = math.degrees(math.atan2(p_one_p_t[0], p_one_p_t[1]))

        # Smooth the angle from the previous angle to avoid inconsistencies in the final angle result

        angle_smoothed = 0.5 * angle_t + (1 - 0.5) * angle_t_pre
        var_angle = abs(angle_smoothed - angle_t_pre)
        var_angle = round(min(max(abs(var_angle), 0.1), 3), 3)

        angle_2_smoothed = 0.5 * angle_2 + (1 - 0.5) * angle_2_pre
        var_angle_2 = abs(angle_2_smoothed - angle_2_pre)
        var_angle_2 = round(min(max(abs(var_angle_2), 0.1), 10), 3)



        time_stamp = time.time()
        if "last_time" not in locals():
            last_time = time_stamp
        elif time_stamp - last_time >= 0.1:
            last_time = time_stamp
            # to do only after sensitivity
            if var_angle > sensitivity_1_min and var_angle <= sensitivity_max_1:
                print(f'Tilt y/x: {round(angle_smoothed, 0)}')
            if var_angle_2 >= sensitivity_2_min and var_angle <= sensitivity_max_2:
                print(f'Tilt y/z: {round(angle_2_smoothed, 0)}')

        angle_t_pre = angle_t
        angle_2_pre = angle_2

        # Creates representative lines in the hand

        cv2.line(img, (int(wrist_[0]), int(wrist_[1])), (int(middle_[0]), int(middle_[1])), (0, 255, 0), 2)
        cv2.line(img, (int(thumb_[0]), int(thumb_[1])), (int(pinky_under[0]), int(pinky_under[1])), (255 , 0 , 0), 2)
        cv2.line(img, (int(thumb_[0]), int(thumb_[1])), (int(wrist_[0]), int(wrist_[1])), (0, 255, 0), 2)
        cv2.line(img, (int(index_[0]), int(index_[1])), (int(wrist_[0]), int(wrist_[1])), (0, 255, 0), 2)
        cv2.line(img, (int(ring_[0]), int(ring_[1])), (int(wrist_[0]), int(wrist_[1])), (0, 255, 0), 2)
        cv2.line(img, (int(pinky_[0]), int(pinky_[1])), (int(wrist_[0]), int(wrist_[1])), (0, 255, 0), 2)

    time.sleep(0.1)

    img = cv2.flip(img, 1)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()
