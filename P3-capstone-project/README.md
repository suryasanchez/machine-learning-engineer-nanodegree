# Capstone Project
## Send custom emails to leads with Machine Learning

Project for Udacity MLDN. [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

The project is about using machine learning to send a custom email to the lead based on the project’s description.

<p align="center">
  <img src="./img/workflow-overview.png" width="50%">
</p>

## [1. Capstone Proposal](https://github.com/suryasanchez/machine-learning-engineer-nanodegree/tree/master/P3-capstone-project/Capstone-Proposal.pdf)

## [2. Capstone Notebook](https://github.com/suryasanchez/machine-learning-engineer-nanodegree/tree/master/P3-capstone-project/Capstone-Notebook.ipynb)

## [3. Capstone Web App](https://github.com/suryasanchez/machine-learning-engineer-nanodegree/tree/master/P3-capstone-project/index.html)

### Environment

* AWS Sagemaker
* kernel: conda_python3

### Summary of the Capstone Notebook

1. Definition

	* 1.1 Project Overview

	* 1.2. Problem Statement

	* 1.3 Metrics

2. Analysis

	* 2.1 Gathering data
		* CRM connection settings
		* Check the format of the data from the API and explore the content
		* Create the dataset

	* 2.2 Data pre-processing
		* Cleaning the data
		* Export to CSV for labeling
		* Import the labeled CSV
		* Reduce the number of class
		* Detect the language of the text
		* Keep only french text
		* Tokenization
		* Bag-of-Words features
		* Save the processed training dataset locally

	* 2.3 Training and testing the model
		* Uploading the training data
		* XGBoost model
		* Testing the model

	* 2.4 Tuning the Hyperparameters
		* Hyperparameter Tuner

	* 2.5 Binary classification
		* Two categories
		* Training of the model
		* Testing the model
		* Tuning the Hyperparameters

	* 2.6 Deploy the model

	* 2.7 Web application
		* Input testing
		* AWS Lambda
		* HTML web app


3. Conclusion

	* 3.1 Reflection

	* 3.2 Improvement

	* 3.3 Application

4. References