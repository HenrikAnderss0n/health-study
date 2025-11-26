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

# 📘 Health Study – Del 2

This part continues the analysis from **Del 1** using the same health dataset.
The focus in Del 2 is on improving the structure of the code and adding some
more advanced analysis.

All analysis for Del 2 is in:  
`health_study_del2.ipynb`

---

## 🧩 Code structure

In Del 2, parts of the code have been moved into separate Python modules to make
the project easier to organise and reuse:

- `analysis/cleaning.py`  
  Contains the function `load_and_clean_data`, which reads the dataset and
  applies the same cleaning steps used in Del 1.

- `analysis/analyzer.py`  
  Contains the class `HealthAnalyzer`, which provides:
  - descriptive statistics  
  - basic visualisations (histogram, boxplot, bar chart)  
  - an extended scatter plot (blood pressure vs age by smoking)  
  - regression models for systolic blood pressure  

The notebook imports these modules and focuses on running the analysis and
explaining the results.

---

## 🔢 Linear algebra and regression

Del 2 introduces multiple linear regression to study how systolic blood pressure
relates to age, weight and cholesterol.  
The predictors are standardised before fitting the models, and R-squared is used
to compare how much variation each model explains.

This satisfies the requirement of including an analysis based on matrix/linear
algebra.

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
health_study_del2.ipynb
```

---


## 📁 Updated project structure

```
health-study/
│
├── analysis/
│   ├── __init__.py
│   ├── cleaning.py
│   └── analyzer.py
│
├── data/
│   └── health_study_dataset.csv
│
├── health_study_del1.ipynb
├── health_study_del2.ipynb
├── README.md
├── requirements.txt
└── .gitignore

```
