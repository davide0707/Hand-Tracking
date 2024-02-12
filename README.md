# Hand TrackingModule with opencv-python and HandDetector
Project developed with opencv-python and HandDetector to detect a hand and calculate the combined angle created between the fingers and the wrist. To then be able to move a motor with the Arduino board.

### Used libraries

- [cv2](https://pypi.org/project/opencv-python/): OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.

- [HandDetector](https://pypi.org/project/HandDectector/): HandDetector is a Python module for hand tracking using OpenCV.

- [time](https://docs.python.org/3/library/time.html): The time module provides various time-related functions.

- [math](https://docs.python.org/3/library/math.html): The math module provides mathematical functions.

- [serial](https://pypi.org/project/pyserial/): PySerial is a Python library to handle serial communication.

### How to get the hand optimally detected for the axes

Place the hand parallel to the video camera by showing as first finger
the little finger and tilt the wrist while keeping the fingers stretched.
