# 🎥 Face Recognition Attendance System

An innovative Face Recognition-based Attendance System that uses deep learning to capture and recognize student faces, update attendance records in real-time using Firebase, and provide a user-friendly GUI for manual database management. This project is inspired by tutorials from **Murtaza Hassan** and **Computer Vision Zone**.

---

## ✨ Features

- **🎬 Real-Time Face Recognition**: Detects and recognizes student faces in real-time using a webcam and deep learning techniques.
- **📊 Firebase Integration**: Seamlessly stores and manages student data and attendance records using Firebase Realtime Database.
- **📈 Automatic Attendance Marking**: Automatically updates attendance status in Firebase for recognized students.
- **🖥️ Manual Database Management GUI**: Built with `Tkinter`, this GUI allows for easy addition, removal, and modification of student records.
- **📤 Export to Excel**: Easily export student data to an Excel file for reporting and analysis.

---

## 📋 Prerequisites

- **Python 3.x**
- Required Python Libraries: `opencv-python`, `numpy`, `face_recognition`, `cvzone`, `firebase-admin`, `tkinter`, `pandas`
- **Dlib and CMake**: Install Visual Studio with **Desktop Development with C++** to compile the necessary C++ libraries required by `face_recognition`.
- A Firebase project with Realtime Database and Storage configured.
- A valid `serviceAccountKey.json` file for Firebase authentication.

---

## 🚀 Setup Instructions

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Sourabh9267/Face-Recognition-Attendance-System-with-Realtime-Firebase-Integration.git
    cd Face-Recognition-Attendance-System-with-Realtime-Firebase-Integration
    ```

2. **Install the Required Packages**:

    ```bash
    pip install opencv-python numpy face_recognition cvzone firebase-admin pandas
    ```

3. **Firebase Configuration**:

   - Place your `serviceAccountKey.json` file in the root directory. This is crucial for Firebase authentication.
   - If you encounter any issues setting up Firebase or generating the `serviceAccountKey.json`, refer to [Murtaza Hassan's tutorial](https://youtu.be/iBomaK2ARyI?t=3975) for step-by-step instructions.

4. **Prepare Student Images**:

   - Use `.png` format for all student images.
   - Name each image file according to the student's unique ID. This convention is essential for accurate identification.

5. **Fill Data Manually**:

   - Run the `studentmanagement.py` script to open the database management GUI.
   - Add each student's details manually once through this interface to ensure the data is correctly synchronized with Firebase.

6. **Generate Encodings**:

   Run the following command to generate the facial encodings required for recognition:

    ```bash
    python EncodeGenerator.py
    ```

   This will create `EncodeFile.p`, containing all known student encodings.

---

## 📂 Running the Project

1. **Run the Face Recognition System**:

    ```bash
    python Main.py
    ```

    This script will start the webcam, detect faces, and update attendance records in real-time.

2. **Run the GUI for Manual Management**:

    ```bash
    python studentmanagement.py
    ```

    Use this GUI to manually add, update, or delete student records and export data to Excel.

---
## ⚙️ Customization Instructions

### ⏱️ Attendance Re-Update Condition

By default, the attendance system allows re-marking of attendance after **30 seconds**. This condition is defined on **Line 114** of `Main.py`:

```python
if secondsElapsed > 30:

```
The value 30 represents the time in seconds after which attendance can be re-marked. You can customize this setting according to your needs:

To Allow Re-marking after 1 Hour:

Replace 30 with 3600 (since there are 3600 seconds in 1 hour):
```python
if secondsElapsed > 3600:
```
To Allow Re-marking after 1 Day:

Replace 30 with 86400 (since there are 86400 seconds in 1 day):
```python
if secondsElapsed > 86400:
```
#### Explanation of the Re-Update Condition:
The variable "secondsElapsed" calculates the time difference in seconds between the current time and the last recorded attendance time for each student. The condition:

```python
if secondsElapsed > X:
```
checks if this time difference (secondsElapsed) exceeds the specified value X. When secondsElapsed is greater than X, the system allows the attendance to be marked again for that student. Adjusting the value of X lets you control the frequency of attendance updates based on your needs:

## 🔍 Code Overview

**📝 Main Components**
- **`Main.py`**: The primary script for face recognition, attendance marking, and database interaction.
- **`studentmanagement.py`**: A GUI application for managing the student database manually.
- **`EncodeGenerator.py`**: A script to generate and store facial encodings.

## 🔧 Key Functions in `Main.py`
- **Face Detection and Recognition**: Utilizes the `face_recognition` library to identify students.
- **Attendance Marking**: Updates Firebase in real-time based on recognized faces.
- **Firebase Operations**: Manages interactions with the Firebase Realtime Database.

**🖥️ GUI Features in `studentmanagement.py`**
- **CRUD Operations**: Add, remove, update student records with ease.
- **Export Functionality**: Export data to Excel for further analysis.

## 🔗 Useful Resources
- **Understanding `face_recognition` Library**: Read [Adam Geitgey's article](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78) to dive deeper into the working of the `face_recognition` library.
- **Project Tutorial by Murtaza Hassan**: Watch the [tutorial video](https://youtu.be/iBomaK2ARyI) that inspired this project.
- **Setting Up Firebase Database**: Follow [this tutorial](https://youtu.be/iBomaK2ARyI?t=3975) for a comprehensive guide on setting up Firebase.

## 🙏 Acknowledgements
- **Thanks to Adam Geitgey** for his fantastic `face_recognition` library. Read his insightful [article](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78) on how this library works.
- **Special Thanks to Murtaza Hassan and Computer Vision Zone** for their inspirational tutorial, which provided a foundation for this project. You can check out their [tutorial here](https://youtu.be/iBomaK2ARyI).

## 🎥 Preview
For a detailed demonstration of this project in action, check out the [Google Drive link](https://drive.google.com/drive/folders/1W-uOhAKS3EEG_gXgOXNpCzCebNdO3_Yk?usp=drive_link) or view the Main project GIF preview below:

![Short Preview Face Recognition Project](https://github.com/user-attachments/assets/f54c7744-cde5-4d4e-8b33-1d1f7243313e)

## Documentation and Project Report for reference
[Face_Recognition_Attendance_System_Documentation.docx](https://github.com/user-attachments/files/16967702/Face_Recognition_Attendance_System_Documentation.docx)




