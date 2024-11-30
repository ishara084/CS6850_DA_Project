# CS6850 Final Project
-  Coding material for final project in CS6850 - Data Analytics
-  Title - Forecasting Walmart Retail Sales with Predictive Data Analysis

### Original dataset: https://kaggle.com/competitions/walmart-recruiting-store-sales-forecasting (2014. Kaggle)

### Project structure
```
|-- root
|-- data_preprocessing.ipynb                                            ------------> Initial Data Pre-processing
|-- libs.py                                                             ------------> Contain common class and methods for data preparation and model evaluation 
|-- predictive_modeling_data_prep.py                                    ------------> Data preparation for predictive modelings
|-- predictive_modeling_Randome_Forest.ipynb                            ------------> Random Forest Classsifier
    |-- data
    |   |-- preproprocessed
    |   |   |-- main.csv                                                ------------> Main dataset after preprocessed, used for EDA
    |   |   |-- main_ML_ready.csv                                       ------------> Main dataset for predictive modeling
    |   |-- source                                                      ------------> Contains source dataset
```

### Instruction
- Original dataset was pre-processed, merged and stored in ```datapreprocessed``` directory and it was used for all analytics and predictive models.
- Install relevant libraries if not already installed. Necessary libraries are mentioned in top of each notebook
- If some cell outputs are empty or showing errors, re-execute the notebook.