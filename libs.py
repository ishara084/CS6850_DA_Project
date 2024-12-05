from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def split_data(df, target_column, test_size=0.2, random_state=42):
    """
    Common method for splitting the dataset into training and testing sets.

    Parameters:
    - df: DataFrame containing the data.
    - target_column: The name of the target column.
    - test_size: Proportion of the dataset to include in the test split.
    - random_state: Seed for reproducibilit.

    Returns:
    - X_train: Training features.
    - X_test: Testing features.
    - y_train: Training target.
    - y_test: Testing target.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test

def evaluate_model(y_true, y_pred, is_holiday):
    """
    Evaluates a regression model using common metrics.

    Parameters:
    - y_true: Actual target values.
    - y_pred: Predicted target values.

    Returns:
    - metrics: A dictionary containing MSE, MAE, RMSE, and R².
    """
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    # Calculate weights for WMAE based on weights given by Walmart on in Kaggle competition
    weights = is_holiday.apply(lambda x: 5 if x else 1).values
    wmae = np.sum(weights * np.abs(y_true - y_pred)) / np.sum(weights)

    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")
    print(f"Weighted Mean Absolute Error (WMAE): {wmae:.2f}")