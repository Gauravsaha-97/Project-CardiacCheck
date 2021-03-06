# Cardiac Check
The various risk factors for developing coronary disease are Age, Sex, Smoking, High Blood Pressure, High Cholesterol Levels, High Heart rate, Exercise induced angina, Thalassemia and more. Cardiovascular Disorder Predictor takes these parameters as input from the user and predicts if he/she has a risk of heart disorder. After entering all the details, clicking on Show Input Data button at the bottom will display the summary of the data entered by the user. The User can then cross-check the data and if there is any mistake, he/she can edit the details and the data will be updated automatically. Then clicking on the Show Test Results button will show the predicted result to the user.

The application is built using Python. The various Python libraries used are Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn and Streamlit. To build the model, Google Colaboratory is used. After reading the data and pre-processing, I tried out different classification models along with hyper-parameter tuning.


The best Accuracy Score is achieved by using K-Nearest Neighbors Algorithm with n_neighbors = 6. The Accuracy achieved is around 90%. So, I have used that model in the web application. The interface of the app is built using Streamlit.

The link to the dataset is [Heart Disorder Data](https://www.kaggle.com/ronitf/heart-disease-uci)
<br>
<br>
Do give a 🌟 if you find this project useful.
