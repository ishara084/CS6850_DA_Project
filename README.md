# CS6850_project
Source code material for final Project in CS6850

### Original dataset: https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data


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