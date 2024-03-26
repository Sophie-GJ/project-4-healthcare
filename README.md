# project-4-healthcare
For this project we set out to apply machine learning to patient health histories to predict the likelihood of certain conditions & diseases.
We pulled several datasets from Kaggle to work on, they can be found in the "datasets" folder.
We worked with four main datasets: patient heart disease data, stroke data, dementia data, and diabetes data for the Pima Indian Tribe.

The datasets can be found here:
* https://www.kaggle.com/datasets/thedevastator/predicting-heart-disease-risk-using-clinical-var
* https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data
* https://www.kaggle.com/datasets/timothyadeyemi/dementia-patient-health-dataset
* https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

We loaded the data into a SQLite database: Healthcare_Data.sqlite using create_sqlite.py.

First we used KerasTuner to create an optimized neural network model for the heart disease and stroke data, found in: 
* heart_disease_Project4_with_markdown_text.ipynb
* stroke_data.ipynb

From there we wanted models with a little more transparency, so we used RandomForest from Scikit-Learn to model all three datasets.
* Ben_test.ipynb (heart disease)
* pima_women_diabetes_project_4.ipynb
* dementia_rf1.ipynb
* dementia_rf2.ipynb

We used transformation pipelines along with OneHotEncoder to transform the categorical data in the dementia dataset.
The original dementia model seemed too accurate/overfitted, so we ran a 2nd model that removed the key variable (age) from the first model.
The second model was just as predictive, so it would seem dementia has some key indicators that make it easier to predict.
