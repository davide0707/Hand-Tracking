# Hand Movement Analysis Using Python, OpenCV, and cvzone

This project processes hand movements using Python along with the libraries OpenCV and cvzone. The goal is to detect and calculate inclination angles relative to two main axes: **y/x** and **y/z**. These angles are derived through real-time tracking of hand landmarks captured via a webcam and are refined to provide stable data.

## 1. Hand Detection and Tracking
Hand detection is performed using the **cvzone** library, which provides the `HandDetector` class. This class identifies the hand within each frame captured by the webcam.

### Key Features:
- A **pre-trained neural network** locates the hand in the image.
- The network extracts **landmarks**, representing specific points on the hand (e.g., wrist, fingers).

Once the hand is detected, the code collects a list of landmarks containing the **x, y, and z coordinates** of each reference point.

---

## 2. Angle Calculation

### 2.1 Angle Along the y/x Axis
The `Angles_yx` class calculates the angle along the **y/x** axis. The process is as follows:
1. Select a specific hand point (e.g., one of the fingers).
2. Calculate the angle between the selected point and the wrist:
   - Compute the differences between the (x, y) coordinates of the chosen point and the wrist to get a **difference vector** (`diff_ang`).
   - Use the `math.atan2()` function to determine the angle between this vector and the x-axis (horizontal axis), in radians.
   - Convert the resulting angle to degrees.

**Result**: The calculated angle represents the hand’s inclination relative to the horizontal axis (**y/x**).

### 2.2 Angle Along the y/z Axis
To calculate the angle along the **y/z** axis:
1. Use the vector connecting the **thumb** and **pinky finger**, based on their respective landmarks.
2. Calculate the angle between this vector and the vertical axis (**y/z**) using the `math.atan2()` function.

---

## 3. Angle Filtering and Smoothing
Sensor data (e.g., landmarks) is often noisy and subject to fluctuations. To achieve stable and accurate values:
- An **exponential moving average** is applied, combining the current angle value with the previous value.
- A **smoothing coefficient** (e.g., 0.5) is used to reduce rapid fluctuations.

**Result**: The smoothed angles provide a more stable representation of hand inclination.

---

## 4. Graphical Visualization
To visualize hand movements:
- The code uses **cv2** to draw lines connecting the hand's landmarks on the screen.
- This graphical representation simplifies understanding and analyzing the hand’s motion and posture.

---
