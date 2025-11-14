# 📘 Health Study – Del 1

This repository contains **Del 1** of the assignment *Individuell uppgift – Hälsostudie*.  
The purpose of this part is to perform basic exploratory data analysis, simulation, confidence intervals and hypothesis testing based on a health dataset.

All analysis for Del 1 is in:  
`health_study_del1.ipynb`

---

## 📄 Dataset

The dataset used in this analysis is stored in:  
`data/health_study_dataset.csv`

It contains the following variables:

- **age** (years)  
- **sex** (M/F)  
- **height** (cm)  
- **weight** (kg)  
- **systolic_bp** (mmHg)  
- **cholesterol** (mmol/L)  
- **smoker** (Yes/No)  
- **disease** (0/1)

---

## 🧪 What is included in Del 1

The notebook contains:

- basic descriptive statistics  
- visualisations (histogram, boxplot, bar chart)  
- a disease prevalence simulation  
- a 95% confidence interval for systolic blood pressure  
- a hypothesis test comparing smokers vs non-smokers  
- a power simulation

---

## ⚙️ Reproducibility

- **Python version:** `3.13.1`
- A fixed random seed is used for reproducibility:

```python
np.random.seed(42)
```

Install required packages:

```bash
pip install -r requirements.txt
```

To run the notebook:

```bash
jupyter notebook
```

Open:

```
health_study_del1.ipynb
```

---

## 📁 Project structure

```
health-study/
│
├── data/
│   └── health_study_dataset.csv
│
├── health_study_del1.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```
