# predictor-project 

# Final Project of IronHack Portugal Data Analytics Full-Time Bootcamp. July 2023 cohort. 

# Predicting Hotel Booking Cancellations

## Business Problem Solving
The primary goal of this project is to develop a model that can predict hotel booking cancellations. By predicting cancellations in advance, hotels can effectively allocate their resources and improve revenue management.

## Stakeholders
The potential stakeholders for this project include hotels, travel agencies, and booking platforms. All of these entities have a vested interest in reducing cancellations to enhance their operations and improve customer satisfaction.

## Steps of the Project


## Step 1: Define the Business Problem and Collect Data

### Define the Problem
Clearly state the problem you're addressing: predicting hotel booking cancellations to optimize revenue and resource management for hotels.
### Collect Data
Download and import the ‘Hotel demand’ dataset from Kaggle. The dataset served as the foundation for the analysis and model development.


## Step 2: Data Preparation and Cleaning

### Data Inspection
Loaded the dataset into a Python environment (VS Code) and inspected its structure, columns, and data types. This step helped understand the data.
### Data Cleaning
Handled missing values by identifying columns with missing values and decided on the appropriate strategy. Additionally, checked for and removed duplicate rows. Finally, examined the numerical features for outliers and decided whether to remove or transform them.
### Data Preprocessing
Converted categorical variables into numerical format using the technique label encoding and normalized the numerical features to ensure they are on the same scale.


## Step 3: Data Analysis and Visualization

### Exploratory Data Analysis (EDA)
Explored the dataset to gained insights into booking patterns, seasonal trends, and the customer demographics. Analyzed the distribution of booking cancellations across different variables. Examined if cancellations vary based on months or seasons. Analyzed booking behaviors based on customer attributes.
### Data Visualization
Created visualizations to illustrate insights from the EDA. 
Coding in Python 
Utilized Python to perform data manipulation tasks such as filtering, concatenating, and aggregating the data.


## Step 4: Feature Selection and Engineering

### Feature Importance 
Used techniques like correlation analysis to identify significant features that contribute to the prediction of cancellations.


## Step 5: Model Selection and Training

### Data Splitting
Split the dataset into training and testing sets using an 80-20 split. 
### Model Selection
Ran multiple a classification algorithms, such as Logistic Regression, Random Forest, and XGBoost, to train predictive models. 
### Model Training
Trained the models using the training data. Adjusted hyperparameters to optimize model performance using the Randomized Search CV technique.

## Step 6: Model Evaluation and Performance Metrics

### Model Evaluation
Evaluated the trained models using the testing data. 
### Comparison and Selection
Compared the performance of different models based on the evaluation metrics. Chose the XGBoost model which had the best overall performance, an incredible 98,3% accuracy score in predicting hotel booking cancellations.


## Step 7: Finalization and Presentation

### Documentation
Documented every step of the project, including the data cleaning, preprocessing, EDA, model selection, training, and evaluation. 
### Visualization for Presentation
Created visualizations using to showcase the key findings, insights, and model performance metrics in a Streamlit Web App. 
### Project Presentation
Prepared a slide-show presentation summarizing the project, its objectives, methodology, key findings, and insights. 

