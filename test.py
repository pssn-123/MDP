import streamlit as st
import base64
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️",
    initial_sidebar_state="collapsed"
)
# Load background image
@st.cache_data
def load_image(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    encoded_image = base64.b64encode(data).decode()
    return encoded_image

image_path = 'website_bg.jpg'  # Replace with the path to your image
encoded_image = load_image(image_path)

# Set page configuration


# Custom CSS to set background image
st.markdown(
    f"""
    <style>
        body {{
            background-image: url('data:image/jpg;base64,{encoded_image}');
            background-size: cover;
            background-repeat: no-repeat;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit app code below
# Add your existing code here...
