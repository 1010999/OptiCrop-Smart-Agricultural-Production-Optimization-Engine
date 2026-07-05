# 🌱 OptiCrop — Smart Agricultural Production Optimization Engine

OptiCrop is a machine learning–powered web application that recommends the most suitable crop to grow based on soil nutrients (Nitrogen, Phosphorus, Potassium), soil pH, and weather conditions (temperature, humidity, rainfall). It helps farmers, agricultural researchers, and policymakers make data-driven decisions for maximizing yield and resource efficiency.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

The **Smart Agricultural Production Optimization Engine (OptiCrop)** integrates key environmental factors — N, P, K levels, soil temperature, humidity, pH, and rainfall — to deliver intelligent crop recommendations. By combining data analysis, machine learning, and a simple web interface, OptiCrop bridges the gap between raw agricultural data and actionable farming decisions.

### Use Cases

| Scenario | Description |
|---|---|
| **Smart Crop Recommendation** | A farmer enters soil and weather details and receives the most suitable crop to plant for maximum yield. |
| **Crop Suitability Assessment** | A user checks whether current soil/climate conditions are compatible with a specific crop. |
| **Agricultural Research & Policy Planning** | Researchers and policymakers analyze crop–environment relationships to design sustainable farming strategies. |

---

## Problem Statement

Farmers often select crops based on tradition or guesswork rather than data, leading to:

- Poor yields from crops mismatched to soil/climate conditions
- Overuse of fertilizers, degrading soil health over time
- Limited awareness of how environmental factors affect productivity
- Economic loss and food insecurity

OptiCrop solves this by using a trained classification model to recommend the optimal crop from 7 simple input parameters.

---

## Features

- ✅ Predicts the best crop from 22 possible crop types
- ✅ Returns a confidence score and top-3 alternative recommendations
- ✅ Clean, responsive web interface (no technical knowledge required)
- ✅ Built on a Logistic Regression model with ~98% test accuracy
- ✅ Includes full exploratory data analysis (EDA) notebook

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | scikit-learn (Logistic Regression, K-Means) |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Model Persistence | Pickle |

---

## Project Architecture

```
                    ┌─────────────────────┐
                    │   Crop Dataset       │
                    │  (N,P,K,temp,        │
                    │   humidity,pH,rain)  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Data Preprocessing   │
                    │  Null check · Outlier │
                    │  removal · Splitting  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Model Training      │
                    │  K-Means · Logistic   │
                    │      Regression       │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Flask Web App        │
                    │  index.html → /predict│
                    │  → result.html        │
                    └───────────────────────┘
```

---

## Dataset

The model is trained on the **Crop Recommendation Dataset**, containing 2,200 records across 22 crop types, each with 100 balanced samples.

| Column | Description | Range |
|---|---|---|
| `N` | Nitrogen content in soil (kg/ha) | 0 – 140 |
| `P` | Phosphorus content in soil (kg/ha) | 5 – 145 |
| `K` | Potassium content in soil (kg/ha) | 5 – 205 |
| `temperature` | Average temperature (°C) | 8 – 44 |
| `humidity` | Relative humidity (%) | 14 – 100 |
| `ph` | Soil pH level | 3.5 – 9.9 |
| `rainfall` | Annual rainfall (mm) | 20 – 298 |
| `label` | Target crop name | 22 classes |

**Crops covered:** apple, banana, blackgram, chickpea, coconut, coffee, cotton, grapes, jute, kidneybeans, lentil, maize, mango, mothbeans, mungbean, muskmelon, orange, papaya, pigeonpeas, pomegranate, rice, watermelon

---

## Project Workflow

1. **Define Problem & Understanding** — business problem, requirements, literature survey, social impact
2. **Data Collection & Analysis** — import libraries, read dataset, univariate/bivariate/multivariate analysis
3. **Data Pre-processing** — null check, outlier handling (IQR method), seasonal crop extraction, train/test split
4. **Model Building** — K-Means clustering, Logistic Regression, evaluation, model saving, prediction
5. **Application Building** — HTML templates, Flask backend, deployment

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/opticrop.git
cd opticrop

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### requirements.txt

```
numpy
pandas
matplotlib
seaborn
scikit-learn
flask
```

---

## Usage

### Run the web application

```bash
python app.py
```

Then open your browser at:

```
https://opticrop-indol.vercel.app/
```

Enter your soil and weather parameters and click **Recommend Best Crop** to get an instant prediction.

### Retrain the model (optional)

If you want to retrain the model from scratch using the dataset:

```bash
python train.py
```

This regenerates `model/crop_model.pkl`, `model/label_encoder.pkl`, and `model/scaler.pkl`.

---

## Model Performance

| Metric | Score |
|---|---|
| Training Accuracy | ~98% |
| Testing Accuracy | ~98% |
| Algorithm | Logistic Regression (multi-class, lbfgs solver) |
| Classes | 22 crops |

A K-Means clustering model is also included for unsupervised exploration of natural crop groupings based on environmental similarity.

---

## Folder Structure

```
opticrop/
│
├── model/
│   ├── crop_model.pkl          # Trained Logistic Regression model
│   ├── label_encoder.pkl       # Encodes/decodes crop names
│   └── scaler.pkl              # Feature scaler
│
├── templates/
│   ├── index.html              # Input form page
│   └── result.html             # Prediction result page
│
├── static/
│   └── style.css                # App styling
│
├── notebooks/
│   └── opticrop_analysis.ipynb # EDA + model training notebook
│
├── Crop_recommendation.csv      # Dataset
├── train.py                     # Model training script
├── app.py                       # Flask backend
├── requirements.txt
├── locustfile.csv
├── results_stats.csv
└── README.md
```

---

## Future Enhancements

- [ ] Add Random Forest / XGBoost models for higher accuracy
- [ ] Integrate a live weather API to auto-fill temperature, humidity, and rainfall by location
- [ ] Add a fertilizer recommendation module
- [ ] Deploy to a cloud platform (Render, Railway, or Heroku)
- [ ] Add a regional map view for area-based recommendations

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- Dataset: Crop Recommendation Dataset (Kaggle)
- Built as part of the OptiCrop project workflow covering problem definition, data analysis, preprocessing, model building, and deployment.
