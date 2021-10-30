#Importing necessary libraries

import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

#Setting the header components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

header = """
<div style="padding:0px;">
<h1 style="color:#ffcc00;text-align:center; font-size:50px;">Cardiac Check🫀</h1>
<h6 style="color:#99ff66;text-align:center; font-size:25px;">Get your results instantly!🤳</h6>
</div>
<br>
<br>
<br>
<br>
<br>
<br>
</body>
"""
st.markdown(header, unsafe_allow_html=True)

#Reading the dataset('heart.csv')

heart_df = pd.read_csv('heart.csv')

#Seperating the dependent(Y) and Independent(X) features

X = heart_df.iloc[:,:-1].values
Y = heart_df.iloc[:,-1].values

#Preprocessing the data

scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)

#Splitting the data into training and testing sets (Train size: 70%, Test size: 30%)

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled,Y,test_size=0.3, random_state=47)

#Function to take input from the user

def user_input():
    header_text = """
    <h2 style="color:#ffdb4d; font-size:25px;">Please Enter Your Test Results👇</h2>
    </div>
    <br>
    <br>
    """
    st.markdown(header_text, unsafe_allow_html=True)
    age_text ="""
    <h5 style="color:#ff9900; font-size:18px;">Please Enter Your Age</h5>
    """
    st.markdown(age_text, unsafe_allow_html=True)
    age = st.number_input('',0,100,0)

    gender_text = """
        <br>
       <h5 style="color:#ff9900; font-size:18px;">Please Select Your Gender</h5>
       """
    st.markdown(gender_text, unsafe_allow_html=True)
    sex = st.selectbox('',("Male", "Female"))

    chestpain_text = """
        <br>
        <br>
       <h5 style="color:#ff9900; font-size:18px;">Please Select Your Chest Pain Type</h5>
       """
    st.markdown(chestpain_text, unsafe_allow_html=True)
    cp = st.radio('',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic"))

    bloodpressure_text = """
        <br>
       <h5 style="color:#ff9900; font-size:18px;">Please Select Your Blood Pressure(mm/Hg) Level</h5>
       """
    st.markdown(bloodpressure_text, unsafe_allow_html=True)
    trestbps = st.slider('',94,200,100)

    cholesterol_text = """
            <br>
           <h5 style="color:#ff9900; font-size:18px;">Please Select Your Serum Cholestoral(mg/dl) Level</h5>
           """
    st.markdown(cholesterol_text, unsafe_allow_html=True)
    chol = st.slider('',100,700,150)

    fbs_text = """
                <br>
               <h5 style="color:#ff9900; font-size:18px;">Please Select Your Fasting Blood Sugar Level</h5>
               """
    st.markdown(fbs_text, unsafe_allow_html=True)
    fbs = st.radio('',("Lower than 120 mg/dl", "Greater than 120 mg/dl"))

    restecg_text = """
        <br>
        <h5 style="color:#ff9900; font-size:18px;">Please Select Your Resting ECG Results</h5>
        """
    st.markdown(restecg_text, unsafe_allow_html=True)
    restecg = st.radio('',("Normal", "ST-T wave abnormality",'Left ventricular hypertrophy'))

    thalach_text = """
          <br>
          <h5 style="color:#ff9900; font-size:18px;">Please Select Your Maximum Heart Rate</h5>
          """
    st.markdown(thalach_text, unsafe_allow_html=True)
    thalach =  st.slider('',60,250,100)

    exang_text = """
          <br>
          <h5 style="color:#ff9900; font-size:18px;">Do You Have Experienced Exercise Induced Angina?</h5>
          """
    st.markdown(exang_text, unsafe_allow_html=True)
    exang = st.radio('',("No", "Yes"))

    oldpeak_text = """
          <br>
          <h5 style="color:#ff9900; font-size:18px;">Please Select Your Exercise Induced ST Depression</h5>
          """
    st.markdown(oldpeak_text, unsafe_allow_html=True)
    oldpeak = st.slider('',0.0,8.0,4.0)

    slope_text = """
              <br>
              <h5 style="color:#ff9900; font-size:18px;">Please Select Your ST Segment Peak Slope</h5>
              """
    st.markdown(slope_text, unsafe_allow_html=True)
    slope = st.radio('',("Upsloping", "Flat", "Downsloping"))

    ca_text = """
            <br>
            <h5 style="color:#ff9900; font-size:18px;">Please Select The Number of major vessels (0-3) colored by Flourosopy</h5>
        """
    st.markdown(ca_text, unsafe_allow_html=True)
    ca = st.selectbox('',(0,1,3))

    thal_text = """
                <br>
                <h5 style="color:#ff9900; font-size:18px;">Please Select Your Thalassemia Type</h5>
            """
    st.markdown(thal_text, unsafe_allow_html=True)
    thal = st.radio('',('Normal','Fixed defect','Reversable defect'))

    space_text = """
    <br>
    <br>
    <br>
    """
    st.markdown(space_text, unsafe_allow_html=True)

    user_data = {}
    user_input_data = {
        'Age': age, 'Sex': sex, 'Chest Pain Type': cp, 'Resting Blood Pressure(mm/Hg)': trestbps, 'Serum Cholestoral(mg/dl)': chol,'Fasting Blood Sugar':fbs,
    'Resting Electrocardiographic Results': restecg,'Maximum heart rate achieved':thalach,'Exercise Induced Angina':exang,'ST depression':oldpeak,
    'Slope':slope,'Number of major vessels':ca, 'Thalassemia': thal
    }

    user_data['Age'] = age

    if sex=="Male":
        user_data['Sex'] = 1
    else:
        user_data['Sex']=0

    if cp=="Typical angina":
        user_data['Chest Pain Type'] = 0
    elif cp=="Atypical angina":
        user_data['Chest Pain Type']=1
    elif cp=="Non-anginal pain":
        user_data['Chest Pain Type']=2
    elif cp=="Asymptomatic":
        user_data['Chest Pain Type']=3

    user_data['Resting Blood Pressure(mm/Hg)'] = trestbps

    user_data['Serum Cholestoral(mg/dl)'] = chol

    if fbs=="Lower than 120 mg/dl":
        user_data['Fasting Blood Sugar'] = 0
    elif fbs=="Greater than 120 mg/dl":
        user_data['Fasting Blood Sugar'] = 1

    if restecg=='Normal':
        user_data['Resting Electrocardiographic Results']=0
    elif restecg=='ST-T wave abnormality':
        user_data['Resting Electrocardiographic Results'] = 1
    elif restecg == 'Left ventricular hypertrophy':
        user_data['Resting Electrocardiographic Results'] = 2

    user_data['Maximum heart rate achieved'] = thalach

    if exang=='No':
        user_data['Exercise Induced Angina'] = 0
    elif exang=='Yes':
        user_data['Exercise Induced Angina'] = 1

    user_data['ST depression'] = oldpeak

    if slope=='Upsloping':
        user_data['Slope'] = 0
    elif slope == 'Flat':
        user_data['Slope'] = 1
    elif slope == 'Downsloping':
        user_data['Slope'] = 2

    user_data['Number of major vessels'] = ca

    if thal=='Normal':
        user_data['Thalassemia'] = 1
    elif thal=='Fixed defect':
        user_data['Thalassemia'] = 2
    elif thal=='Reversable defect':
        user_data['Thalassemia']=3

    features = pd.DataFrame(user_data, index = [0])
    user_input_features = pd.DataFrame(user_input_data, index = [0])

    return features, user_input_features

user_data_input, user_input_features = user_input()

#Initializing the KNN Classifier and do the prediction

classifier = KNeighborsClassifier(n_neighbors = 6)
classifier.fit(X_train, Y_train)
prediction = classifier.predict(user_data_input)

#Display the entered data and predicted results to the user

if st.button("Show Input Data"):
    user_input_header = """
    <h2 style="color:#ffdb4d; font-size:20px;">Please Check Your Details👇</h2>
    </div>
    """

    st.markdown(user_input_header, unsafe_allow_html=True)
    brk = """
        <br>
        """
    st.write(user_input_features)
    st.markdown(brk, unsafe_allow_html=True)
    st.success("Your details have been loaded successfully!")


if(st.button("Show Test Results")):
    st.subheader('Test Results:')
    if prediction == 0:
        success_text = """
            <h2 style="color:#99ff33; font-size:20px;">Risk of Heart Disease: NO. Your heart is healthy😎</h2>
            """
        st.markdown(success_text, unsafe_allow_html=True)
        st.balloons()
    elif prediction == 1:
        fail_text= """
            <h2 style="color:#ff1a1a; font-size:20px;">Risk of Heart Disease: YES. Please consult a doctor😰</h2>
            """
        st.markdown(fail_text, unsafe_allow_html=True)
