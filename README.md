# CS6850 Final Project
-  Coding material for final project in CS6850 - Data Analytics
-  Title - Forecasting Walmart Retail Sales with Predictive Data Analysis

### Original dataset: https://kaggle.com/competitions/walmart-recruiting-store-sales-forecasting (2014. Kaggle)

### Project structure
```
root
|-- data_preprocessing.ipynb                                            ------------> Initial Data Pre-processing
|-- libs.py                                                             ------------> Contain common class and methods for data preparation and model evaluation 
|-- EDA_summarization_visualization.ipynb                               ------------> EDA Data exploration and summarization
|-- predictive_modeling_data_prep.ipynb                                 ------------> Data preparation for predictive modelings
|-- predictive_modeling_bias_evaluation.ipynb                           ------------> Bias and Fairness evaluation of predictive models
|-- predictive_modeling_Linear_Regression.ipynb                         ------------> Linear Regression Classifier
|-- predictive_modeling_Decision_Tree.ipynb                             ------------> Decision Tree Classsifier
|-- predictive_modeling_Random_Forest.ipynb                             ------------> Random Forest Classsifier
|-- predictive_modeling_XGBoost.ipynb                                   ------------> XGBoost Classsifier
    |-- data
    |   |-- preproprocessed
    |   |   |-- main.csv                                                ------------> Main dataset after initial preprocessing, used for EDA
    |   |   |-- main_ML_ready.csv                                       ------------> ML ready dataset for predictive modeling (After processing main.csv)
    |   |-- source                                                      ------------> Contains original dataset from Kaggle
```

### Instruction

- Install relevant libraries if not already installed. Necessary libraries are mentioned in top of each notebook
- Original dataset was pre-processed, merged and stored in ```data\preprocessed``` directory and it was used for all analytics and predictive models.
- If some cell outputs are empty or showing errors, re-execute the notebook.