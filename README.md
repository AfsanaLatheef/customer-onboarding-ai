# customer-onboarding-ai
YOLOV8-based document detection and orientation correction for customer onboarding 

## 📌 Overview
This project automates customer onboarding by detecting and validating key documents using a YOLOv8-based AI model. 
Supported documents:
- Aadhar Card
- PAN Card
- Voter ID
- Bank Document
- Live Image Capture

The model is trained to recognize documents in multiple orientations (0°, 90°, 180°, 270°). 
If a document is uploaded in a rotated orientation, the system automatically detects the angle and rotates it back to the correct 0° orientation for accurate detection.

---

## 🚀 Features
- Document Detection: Identifies Aadhar, PAN, Voter ID, and Bank documents.
- Orientation Handling: Supports rotation correction for 0°, 90°, 180°, and 270°.
- Live Image Capture: Adds real-time verification with a live image.
- YOLOv8 Backbone: Fast and accurate object detection.

---

## 🛠️ Tech Stack
- YOLOv8 (Ultralytics)
- Python
- OpenCV (for image rotation and preprocessing)
- PyTorch

---

## 📂 Dataset
The dataset used for training contains sensitive personal information and will not be shared. 
If you want to replicate this project, you can create your own dataset by collecting sample document images and labeling them using tools like [LabelImg](https://github.com/heartexlabs/labelImg).

---

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/your-username/customer-onboarding-ai.git
cd customer-onboarding-ai

# Install dependencies
pip install -r requirements.txt



📊 Results
High accuracy across multiple document types.

Robust detection even with rotated inputs.

Faster onboarding process with automated validation.


