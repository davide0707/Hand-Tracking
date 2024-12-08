# Hand Movement Analysis and Control Using Python, OpenCV, and cvzone

This project explores hand movement analysis and control using Python along with the libraries OpenCV, cvzone, and other utility modules. The system detects hand landmarks, calculates inclination angles, and enables motor control via Arduino by combining the angle created between fingers and the wrist.

---

## 1. Hand Detection and Tracking

Hand detection is performed using the **cvzone** library, specifically the `HandDetector` class, and OpenCV for image processing.

### Key Features:
- A **pre-trained neural network** locates the hand in the image and extracts landmarks (e.g., wrist, fingers).
- The system tracks **x, y, and z coordinates** of each reference point on the hand.

---

## 2. Angle Calculation

### 2.1 Angle Along the y/x Axis

The `Angles_yx` class calculates the angle along the **y/x axis** as follows:
1. Select a specific hand point (e.g., one of the fingers).
2. Calculate the angle between the selected point and the wrist:
   - Compute the differences between the (x, y) coordinates of the chosen point and the wrist.
   - Use the `math.atan2()` function to determine the angle in radians.
   - Convert the resulting angle to degrees.

**Result:** The calculated angle represents the hand’s inclination relative to the horizontal axis (y/x).

### 2.2 Angle Along the y/z Axis

To calculate the angle along the **y/z axis**:
1. Use the vector connecting the **thumb** and **pinky finger** landmarks.
2. Calculate the angle between this vector and the vertical axis (y/z) using the `math.atan2()` function.

---

## 3. Angle Filtering and Smoothing

Sensor data is often noisy. To achieve stable values:
- Apply an **exponential moving average**, combining the current angle value with the previous value.
- Use a **smoothing coefficient** (e.g., 0.5) to reduce rapid fluctuations.

**Result:** The smoothed angles provide a more stable representation of hand inclination.

---

## 4. Graphical Visualization

The code uses **OpenCV** (`cv2`) to draw lines connecting the hand’s landmarks on the screen. This graphical representation simplifies understanding and analyzing hand movements.

---

## 5. Motor Control Integration

The calculated angle is utilized to control a motor via Arduino. This process involves:
- Detecting the hand and calculating the combined angle between the fingers and the wrist.
- Using the `pyserial` library for serial communication with the Arduino board.

---

## Libraries Used

- [cv2](https://pypi.org/project/opencv-python/): OpenCV for computer vision tasks.
- [cvzone](https://pypi.org/project/cvzone/): Simplifies hand tracking and detection.
- [time](https://docs.python.org/3/library/time.html): Provides time-related functions.
- [math](https://docs.python.org/3/library/math.html): Provides mathematical functions.
- [serial](https://pypi.org/project/pyserial/): Handles serial communication with Arduino.

---

## Optimal Hand Positioning

To ensure optimal hand detection for the axes:
- Place your hand parallel to the webcam.
- Show the little finger first and tilt the wrist while keeping fingers stretched.
