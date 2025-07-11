# 🔍 Criminal Detection System

The **Criminal Detection System** is a Python-based facial recognition application designed to help in identifying individuals by matching their facial features with a pre-existing criminal database. This system leverages image processing techniques and machine learning algorithms using **OpenCV**, **Tkinter GUI**, and a **MySQL backend** for managing records. The goal is to streamline criminal identification through a semi-automated and user-friendly desktop application.

---

## 📌 Project Overview

In an era of rising crime rates, this system assists investigation departments by:
- Automatically detecting and identifying suspects from static images or real-time webcam feed.
- Storing and managing criminal profiles (images + demographic/criminal details) securely.
- Supporting accurate recognition even under varying lighting conditions using **LBPH (Local Binary Patterns Histogram)** algorithm.

---

## 🎯 Features

- ✅ **Criminal Registration**: Upload 5+ facial images per criminal and enter demographic/criminal information.
- 🧠 **Face Recognition**: Uses Haar Cascades for face detection and LBPH for facial recognition.
- 📸 **Image-Based Detection**: Upload an image and identify known criminals.
- 🎥 **Real-Time Surveillance**: Webcam-based continuous face detection and recognition.
- 🗂️ **Profile Management**: Stores face samples and profile pictures locally, along with MySQL record linkage.

---

## 🛠️ Technologies Used

| Area              | Tools/Technologies                           |
|-------------------|----------------------------------------------|
| Programming       | Python 3.x                                   |
| GUI               | Tkinter                                      |
| Computer Vision   | OpenCV (cv2), Haar Cascade, LBPH             |
| Database          | MySQL, MySQL Connector                       |
| Image Handling    | PIL (Pillow)                                 |
| Other             | Threading, File I/O, OS                      |

---

## 📁 Project Structure
Criminal_Detection_System/
│
├── face_samples/ # Directory for storing training images
├── profile_pics/ # Profile picture for each criminal
├── home.py # Main application launcher
├── register.py # Handles registration UI & logic
├── facerec.py # Face detection and recognition functions
├── surveillance.py # Webcam stream + detection logic
├── dbHandler.py # MySQL DB connection and data insertion
├── haarcascade_frontalface_default.xml # Haar Cascade classifier for face detection
├── UI assets/ # logo.png, back.png, navigation buttons
└── README.md # Project documentation
