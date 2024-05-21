import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")



# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))


# loading the saved models

diabetes_model = pickle.load(open('FINAL_MDP\saved_model\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('FINAL_MDP\saved_model\heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('FINAL_MDP\saved_model\parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['HomePage','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Liver Disease Prediction',
                            'Lung Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['house','activity', 'heart', 'person',"bag-heart","lungs"],
                           default_index=0)

page_bg_img = '''
 <style>
 body {
 background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
 background-size: cover;
 }
 </style>
 '''

st.markdown(page_bg_img, unsafe_allow_html=True)

if selected == 'HomePage':


    # page title
    st.markdown(
        "<h1 style='text-align: center; background-color: green; color: white; padding: 20px; width: 100%;'>Multiple Disease prediction using Python</h1>",
        unsafe_allow_html=True
    )



    # Custom CSS for text styling
    st.markdown(
        """
        <style>
        body {
        background-color: #e6ffe6; /* Light green background color */
    }
        .big-text {
            font-size: 18px;
            text-align: justify;
        }
        .steps { 
        font size: 14px;
        text-align: justify;
         
        </style>
        """,
        unsafe_allow_html=True
    )


    # Title and introduction
    st.markdown(
        "<p class='big-text'>In recent years, technology and healthcare have come together in exciting ways. "
        "Predictive analytics emerges as a powerful tool in disease prevention and management. "
        "By using the huge amount of data collected in healthcare systems, predictive models can spot "
        "potential health issues early, intervene promptly, and create personalized treatment plans. "
        "This proactive healthcare approach not only improves patient outcomes but also contributes "
        "to the sustainability of healthcare systems worldwide.</p>"
        "<br>",
        unsafe_allow_html=True
    )

    # Predefined Images
    predefined_images = ["images_for_use\heart_image_one.jpg", "images_for_use\diabetes_image_sec.jpg", "images_for_use\parkinson_image_three.jpg",
                         "images_for_use\liver_disease_four.jpg"]
    images = [Image.open(image_path) for image_path in predefined_images]

    # Display images side by side
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(images[0], caption="Heart Disease", use_column_width=True)

    with col2:
        st.image(images[1], caption="Diabetes", use_column_width=True)

    with col3:
        st.image(images[2], caption="Parkinson's Disease", use_column_width=True)

    with col4:
        st.image(images[3], caption="Liver Disease", use_column_width=True)


    # Project description
    st.markdown(
        "<p class='big-text'>This project presents a novel approach: a multi-disease prediction model powered by machine learning. "
        "This model analyzes various data points to predict the risk of developing multiple diseases simultaneously. "
        "This offers several advantages:</p>",
        unsafe_allow_html=True
    )
    advantages = [
        "<b>Faster and more precise:</b> Machine learning algorithms can analyze data rapidly and identify patterns that might be missed by humans.",
        "<b>Reduced human error:</b> Algorithms are less susceptible to biases and can provide more consistent results.",
        "<b>Proactive healthcare:</b> Early risk assessment empowers individuals to take preventive measures and manage their health proactively."
        "<br/>"
    ]

    # Displaying advantages
    for advantage in advantages:
        st.markdown(f"<p class='big-text'>{advantage}</p>", unsafe_allow_html=True)





        #How to Use the Model
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    "<h2 style='text-align: center; color: white; background-color: red;'>How to Use the Model</h2>",
    unsafe_allow_html=True
)
    st.markdown("<br>", unsafe_allow_html=True)

# STEP 1
    st.markdown("<h2 style='text-align: center; color: black;text-decoration: underline;'>STEP 1 </h2>", unsafe_allow_html=True)
    image_path_1 = "ss_1.png"
    description_1 = "<b>Choose the disease model:</b> Select the specific disease you want to predict from the available options."


    col1, col2 = st.columns([1, 2])
    with col1:
     st.image(image_path_1, caption="Image", width=300, use_column_width=False)
    with col2:
     st.markdown(
        f"<div style='display: flex; flex-direction: column; justify-content: center; height: 300px;'>"
        f"<h3 style='text-align: center;'>{description_1}</h3>"
        f"</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)


# STEP 2
    st.markdown("<h2 style='text-align: center; color: black;text-decoration: underline;'>STEP 2 </h2>", unsafe_allow_html=True)
    image_path_2 = "ss_2.png"
    description_2 = "Input required parameters: Enter the necessary medical data and parameters relevant to the selected disease."


    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_path_2, caption="Image", width=500, use_column_width=True)
    with col2:
        st.markdown(
        f"<div style='display: flex; flex-direction: column; justify-content: center; height: 120px;'>"
        f"<h3 style='text-align: center;'>{description_2}</h3>"
        f"</div>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)


# STEP 3
    st.markdown("<h2 style='text-align: center; color: black;text-decoration: underline;'>STEP 3 </h2>", unsafe_allow_html=True)
    image_path_2 = "ss_3.png"  # Replace "ss_1.png" with the path to your image
    description_2 = "Retrieve predictions: Click on the button to generate predictions based on the provided parameters and medical data."


    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_path_2, caption="Image", width=300, use_column_width=False)
    with col2:
        st.markdown(
        f"<div style='display: flex; flex-direction: column; justify-content: center; height: 200px;'>"
        f"<h3 style='text-align: center;'>{description_2}</h3>"
        f"</div>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

        #About us
    st.markdown(
    "<h2 style='text-align: center; color: white; background-color: green;'>About Us</h2>",
    unsafe_allow_html=True
       )
    st.markdown("<br>", unsafe_allow_html=True)

# Diabetes Prediction

if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)






    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown("<h2 style='text-align: center; color: black;text-decoration: underline;'>More on our diabetes prediction model</h2>",
                unsafe_allow_html=True)

    image_path_2 = "ss_3.png"  # Replace "ss_1.png" with the path to your image
    st.image(image_path_2, caption="Image", width=300, use_column_width=False)







# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


