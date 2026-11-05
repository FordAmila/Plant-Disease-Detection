# Plant Disease Detection 🌿🔍

A web application and dashboard designed to detect and classify plant diseases using deep learning. 

## 📖 Overview
This project provides a user-friendly web interface to upload images of plant leaves and identify potential diseases. It utilizes a trained Keras model (`.keras`) to run inferences and displays the results through a web application. It also includes a dashboard for monitoring and analytics.

## 🚀 Features
* **Disease Classification:** Upload images of plant leaves to quickly identify diseases.
* **Web Application:** A responsive interface built with HTML, CSS, and JavaScript.
* **Dashboard:** An integrated dashboard for managing data and viewing classification insights.
* **Easy Startup:** Comes with a `start.bat` file for quick local deployment on Windows.

## 🛠️ Technologies Used
* **Backend & Machine Learning:** Python, Keras (Deep Learning)
* **Frontend:** HTML5, CSS3, JavaScript
* **Version Control:** Git, Git LFS (for large `.keras` model files)

## 📂 Project Structure
```text
Plant-Disease-Detection/
│
├── dashboard/          # Source code for the analytics/management dashboard
├── webapp/             # Source code for the main user-facing web application
├── start.bat           # Windows batch script to initialize and run the application
├── .gitattributes      # Git configuration (includes Git LFS tracking for models)
└── README.md           # Project documentation
