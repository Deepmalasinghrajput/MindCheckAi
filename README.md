# MindCheckAi

# MindCheck AI - Mental Health Prediction

MindCheck AI is a machine learning-powered application that assists in distinguishing between **Depression** and **ME/CFS (Chronic Fatigue Syndrome)** using user-input health and lifestyle data.

This project demonstrates how artificial intelligence can be applied to mental health support and early screening through a clean, interactive web interface built using Streamlit.

---

## 🔍 Objective

To build an intelligent and user-friendly tool that predicts the likelihood of Depression or ME/CFS based on non-invasive health indicators such as:

- Sleep quality
- Brain fog level
- Physical pain
- Stress
- Fatigue and more

---

## 💡 Features

- Real-time predictions using K-Nearest Neighbors (KNN)
- Intuitive UI with sliders and dropdowns
- Interactive results and insights
- Built-in awareness around overlapping symptoms
- No login or data storage required

---

## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Joblib**
- **Matplotlib** & **Seaborn** (for training and visualizations)

---

## 📁 Files Included

| File / Folder         | Description |
|-----------------------|-------------|
| `app.py`              | Main Streamlit app script |
| `knn_model.pkl`       | Trained machine learning model |
| `scaler.pkl`          | Scaler used during model training |
| `columns.pkl`         | Input feature structure |
| `mental.jpg`          | Sidebar image |
| `requirements.txt`    | Dependencies for environment setup |
| `README.md`           | Project documentation |
| `training.ipynb`      | Optional: Model training notebook |

---

## 🚀 How to Run Locally

1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/mindcheck-ai.git
   cd mindcheck-ai
