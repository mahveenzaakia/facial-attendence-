# 🧠 Face Recognition Attendance System

A real-time face recognition-based attendance system built using **Python**, **OpenCV**, and **Streamlit** with a sleek UI and automated attendance logging.

![UI](Face%20Recognition%20UI%20Design.png)

---

## 🚀 Features

- 🔐 **Face Registration**: Register new faces using your webcam.
- 🧾 **Real-Time Attendance**: Automatically detect and log attendance with face recognition.
- 📊 **Attendance Logs**: View attendance logs filtered by date directly in the app.
- 🎨 **Modern UI**: Responsive and aesthetic frontend powered by Streamlit with background overlays.
- 🗣️ **Voice Feedback**: Audio confirmation when attendance is marked.

---

## 🗂️ Project Structure

```
📁 data/                  → Trained data files (faces, labels, Haar Cascade)
📁 Attendance/            → Automatically generated attendance CSVs
📄 app.py                 → Auto-refreshing view-only attendance log
📄 test.py                → Core face recognition & attendance script
📄 add_faces.py           → Script to register new faces
📄 frontend.py            → Streamlit UI to interact with system
🖼️ wallpaper.jpg          → UI background
🖼️ Face Recognition UI Design.png → UI screenshot
```

---

## ⚙️ Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Install required packages**:
   ```bash
   pip install opencv-python streamlit pandas scikit-learn pywin32
   ```

3. **Ensure these files exist**:
   - `data/haarcascade_frontalface_default.xml`
   - `data/faces_data.pkl` and `data/names.pkl` will be generated automatically after registration

---

## 🧑‍🏫 How to Use

### 📋 1. Register a Face
```bash
python add_faces.py
```
- Enter your name.
- Press `q` when 100 images are collected.

### 🕵️ 2. Start Attendance System
```bash
python test.py
```
- Detects faces and logs attendance in `Attendance/Attendance_<date>.csv`.
- Press `o` to mark attendance, `q` to quit.

### 🌐 3. Run UI (Frontend)
```bash
streamlit run frontend.py
```
- Register face, start recognition, or view today’s log via buttons.

---

## 📁 Attendance Log Format

Each file is saved as:

```
Attendance/Attendance_DD-MM-YYYY.csv
```

Format:
| NAME | TIME |
|------|------|
| John | 09:45:32 |
| Alice | 10:01:45 |

---

## 📝 Credits

- OpenCV — for image processing and face detection
- Scikit-learn — KNN classification
- Streamlit — frontend UI
- pywin32 — speech API (Windows only)

---

## 📌 Notes

- Make sure webcam access is enabled.
- Voice feedback (`pywin32`) works only on **Windows**.
- All attendance files are saved locally in the `Attendance` folder.

---

## 📸 Screenshots

![App Preview](face-attendance-machine.webp)