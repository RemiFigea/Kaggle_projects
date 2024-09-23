# Car Prices Prediction

## Overview

The **Car Prices Prediction** project is a Kaggle competition aimed at predicting the prices of used cars. The objective is to build models that accurately forecast car prices based on various features such as make, model, year, milage, and more.

## Project Structure

```
/Car_Prices_Prediction
	- car_prices_prediction_LGBM.ipynb
	- car_prices_prediction_KERAS.ipynb
	- hyperparameters_analyse_KERAS.ipynb
	/data
		- train.csv
		- test.csv
		- sample_submission.csv
	/scripts
		- visualisation.py
	/results
		- (To be added)
  	- requirements.txt
  	- README.md
```

1. **`car_prices_prediction_LGBM.ipynb`**
   - This notebook focuses on using the LightGBM model for regression.

2. **`car_prices_prediction_KERAS.ipynb`**
   - This notebook employs a deep learning approach using Keras.
3. **`hyperparameters_analyse_KERAS.ipynb`**
   - This notebook focused on hyperparameters optimization of a simple Keras model.

## Data

- **`train.csv`**: The training dataset containing features and target prices for used cars.
- **`test.csv`**: The test dataset used for making predictions.
- **`sample_submission.csv`**: A sample submission file to guide the format for the final submission.

## Scripts

- **`visualisation.py`**: Contains code for data plotting.

## Results

- Results will be added here after running the models.

## Installation

To run the notebooks and scripts, you need to install the required packages. You can install them using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preparation:**
  - Place your dataset files (train.csv, test.csv, and sample_submission.csv) in the /data directory.

2. **Running Notebooks:**
  *Note: You may need to adapt the file paths specified in the notebooks, as they were loaded from the Kaggle platform, which has its own architecture.*

  - Open the notebook.
  - Follow the instructions within the notebooks to train the models and generate predictions.

3. **Generating Predictions:**
  - Run the notebooks to produce the predictions and save the results in the /results directory.