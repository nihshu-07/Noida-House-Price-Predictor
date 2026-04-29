# 🏠 Noida House Price Predictor

A machine learning based web application that predicts house prices in Noida using user inputs like location, BHK, and area. Built using **Python, Scikit-learn, and Streamlit**.

---

## 🚀 Project Overview

This project aims to solve a real world problem of estimating house prices based on key property features. It leverages data analysis and machine learning to provide accurate predictions along with similar property recommendations.

---

## 🎯 Problem Statement

House buyers often struggle to estimate fair property prices due to lack of data insights.
This project helps users:

* Predict property prices instantly
* Understand price trends based on location and size
* Explore similar properties from the dataset

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn (EDA phase)
* **Web Framework:** Streamlit
* **Model:** Regression Model (trained on Noida housing dataset)

---

## 📊 Features

* 📍 Select Location (Noida sectors)
* 🛏 Choose number of BHK
* 📐 Enter area in square feet
* 💰 Get predicted house price (in Lakhs/Crores)
* 🏘 View similar properties from dataset
* 🎨 Clean and interactive UI

---

## 🧠 Machine Learning Workflow

1. Data Cleaning & Preprocessing
2. Feature Engineering (e.g., area per BHK)
3. Exploratory Data Analysis (EDA)
4. Outlier Detection & Removal
5. Model Training & Selection
6. Model Deployment using Streamlit

---

## 📁 Project Structure

```
Noida-House-Price-Predictor/
│-- app.py
│-- house_price_model.pkl
│-- cleaned2.csv
│-- notebooks/
│   │-- 01-Preprocessing.ipynb
│   │-- 02-FE.ipynb
│   │-- 03-EDA.ipynb
│   │-- 04-Outliers.ipynb
│   │-- 05-Model Selection.ipynb
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/noida-house-price-predictor.git
cd noida-house-price-predictor
```

### 2. Create Virtual Environment (optional but recommended)

```
python -m venv venv
venv\\Scripts\\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

If requirements.txt is not available:

```
pip install streamlit pandas numpy scikit-learn
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📈 Sample Output

* Input: 3 BHK, Sector 137, 1500 sq.ft
* Output: ₹ 1.25 Cr (Predicted Price)
* Also displays similar properties from dataset

---

## 🔥 Key Highlights

* End-to-end ML pipeline (EDA → Model → Deployment)
* Real-world dataset and problem solving approach
* Interactive UI using Streamlit
* Business-focused insights for users

---

## 🚧 Future Improvements

* Add price trend visualization by location
* Integrate map view for properties
* Add recommendation: Budget / Premium classification
* Deploy on cloud (Streamlit Cloud / AWS)
* Add feature importance explanation

---

## 🙋‍♀️ Author

**Niharika Tyagi**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---
