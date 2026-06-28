# Machine Learning Projects

This repository contains hands-on machine-learning notebooks, datasets, trained models, and a small Streamlit application. The projects cover regression, classification, clustering, exploratory data analysis, and model deployment.

## Projects

| Project | Main files | Description |
| --- | --- | --- |
| House price prediction | `housepriceprediction.ipynb`, `housepricepridction2.ipynb`, `HousePricePrediction.xlsx`, `model.pkl` | Trains a regression model to estimate house prices. |
| House price web app | `app.py` | Streamlit interface that loads `model.pkl` and predicts a price from eight property features. |
| Diabetes prediction | `predictive analysis in diabetes.ipynb`, `diabetes.csv`, `diabetes_model.pkl` | Explores diabetes data and builds a predictive classification model. |
| Support Vector Machines | `SVM.ipynb`, `Hands-On Implementation of SVM.ipynb`, `WineQT.csv` | SVM experiments and a wine-quality classification exercise. |
| Decision trees | `Decision tree implementation.ipynb` | Practical decision-tree implementation. |
| K-means clustering | `kmean_clustering.ipynb`, `data.csv` | Clustering analysis using online retail transaction data. |
| Visualizations | `boxplot.png`, `boxplot1.png`, `boxplot2.png`, `correlation_heatmap.png` | Generated plots from exploratory data analysis. |

## Getting started

### 1. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install the common dependencies

```powershell
pip install jupyter numpy pandas matplotlib seaborn scikit-learn streamlit openpyxl
```

### 3. Open the notebooks

```powershell
jupyter notebook
```

Select a notebook from the Jupyter interface and run its cells in order. Keep the associated dataset in the repository root so relative file paths continue to work.

## Run the Streamlit app

From the repository root, run:

```powershell
streamlit run app.py
```

The app asks for area, bedrooms, bathrooms, stories, parking, main-road access, guest-room availability, and basement availability. It then uses the saved `model.pkl` model to estimate the house price.

## Repository notes

- The `.pkl` files are serialized trained models; load them only from a trusted source.
- `data.csv` is the largest file in the repository and contains online retail transaction data.
- The notebooks may install or import additional packages depending on the experiment.
- Run scripts and notebooks from the repository root because several files use relative paths.

## Suggested workflow

1. Explore the relevant dataset and notebook.
2. Run every notebook cell in order to reproduce preprocessing, training, and evaluation.
3. Save a newly trained model only after checking its evaluation metrics.
4. Start the Streamlit app to test house-price predictions interactively.
