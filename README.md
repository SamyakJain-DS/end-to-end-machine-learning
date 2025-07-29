# Machine Learning Models Collection

## 🔗 Live App
Access the live deployed project at [https://samyak-jain-ml.streamlit.app/](https://samyak-jain-ml.streamlit.app/)
<img width="1920" height="965" alt="image" src="https://github.com/user-attachments/assets/f0d2bc3c-ba66-4d40-97e3-9b26e2029fcb" />

## 📄 Overview
This project moves beyond theoretical exercises to solve two distinct, real-world business problems. An end-to-end data science project involves the entire lifecycle, from problem formulation to deploying a model into production for practical use. There are two end-to-end machine learning pipelines, each deployed as an interactive Streamlit webpage (see the Live App link above). It includes: 
- Flight Ticket Price Prediction, a regression problem, and
<img width="1920" height="968" alt="image" src="https://github.com/user-attachments/assets/db0cd796-2b3f-42a7-9ef7-d9848697b2a8" />

- Customer Attrition Prediction for a Financial Institute, a classification problem.
<img width="1920" height="968" alt="image" src="https://github.com/user-attachments/assets/5159567b-8a3f-4106-85cb-03404cc47634" />

The focus is on thorough `data preprocessing`, `model comparison`, and `hyperparameter tuning` using reproducible `pipelines`. All steps – from raw data to final prediction – are encapsulated in scikit-learn pipelines to ensure consistency and prevent data leakage.
In the introduction of this README, you can access the live Streamlit deployment here for real-time predictions.

## 🗂️ Data Sources
- Flight Ticket Price Dataset: Sourced from a [Kaggle competition](https://www.kaggle.com/competitions/mlp-term-2-2025-kaggle-assignment-1) on flight ticket prices. The task is to predict ticket price from features like airline, source, destination, etc.
- Customer Attrition Dataset: Sourced from a [Kaggle competition](https://www.kaggle.com/competitions/mlp-term-2-2025-kaggle-assignment-2) on financial customer churn. The goal is to predict whether a customer will leave (attrition) based on account metrics and demographics.

## 📊 Methodology
- **Preprocessing & Pipelines:**
   - All data transformations (encoding categoricals, scaling, feature engineering, etc.) are done via scikit-learn Pipeline objects. Pipelines allow chaining preprocessing and model fitting into one workflow, supporting joint hyperparameter tuning and avoiding train-test leakage. Random seeds are fixed and cross-validation splits are used consistently to ensure reproducibility.
- **Model Selection and Tuning:**
  - For Flight Price Regression, we evaluated several regressors and found that HistGradientBoostingRegressor performed best. This histogram-based gradient boosting is known to train much faster on large datasets and handle missing values natively. Hyperparameters (like learning rate, tree depth) were tuned via grid search CV.
  - For Customer Attrition Classification, we tested various classifiers and selected XGBClassifier. XGBoost is a powerful gradient boosting implementation with built-in regularization and fast training. We tuned its parameters (e.g., max_depth, n_estimators) using cross-validation.

## ✅ Interpretative Analysis
- Regression Success:
   - The `HistGradientBoostingRegressor` demonstrates exceptional predictive power, explaining almost `97%` of the variance in flight prices on both cross-validation and unseen test data.
   - The close alignment between the `cross-validation score` (0.9675) and the `test score` (0.9646) indicates a robust, well-generalized model that is not overfitting to the training data.
- Classification Strategy:
   - For the Customer Attrition model, the primary evaluation metric is `Recall` (0.7551), which was intentionally optimized over `Precision` (0.5428). This strategic decision is driven by the business context.
   - The cost of a false negative—failing to identify a customer who then leaves—is significantly higher than the cost of a false positive—unnecessarily targeting a loyal customer with a retention offer.
   - By maximizing recall, the model correctly identifies over `75%` of the customers who are genuinely at risk of churning. This ensures that the marketing team is alerted to the largest possible pool of at-risk customers, directly supporting the core business goal of minimizing churn and protecting revenue.
   - The `F1-Score` of `0.6315` provides a healthy balance, but the emphasis on recall reflects a model tailored to a specific business need.
 
## 🔧 Technical Stack
| Category | Technologies |
|----------|--------------|
| Core Language | Python 3.x |
| Data Manipulation & Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Data Visualization | Matplotlib |
| Web App & Deployment | Streamlit |
| Development Environment | Jupyter Notebooks, PyCharm |

## 🔁 Setup and Local Deployment
To run this project on your local machine, please follow these steps. This process mirrors standard development practices for creating reproducible environments.   

- Clone the repository:
  `bash`
  ```bash
  git clone https://github.com/SamyakJain-DS/end-to-end-machine-learning.git
  cd end-to-end-machine-learning
  ```
- Install the required dependencies:
  `bash`
  ```bash
  pip install -r requirements.txt
  ```
- You're All Set!
