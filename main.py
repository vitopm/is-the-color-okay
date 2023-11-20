import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

st.set_page_config(
    page_title="Is the color okay?",
    page_icon="🎨",
    )

def analyze_image(image):
    # Convert image to grayscale for brightness analysis
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    # Calculate the average brightness
    average_brightness = np.mean(gray_image)

    # Define threshold values for dark and bright
    dark_threshold = 100
    bright_threshold = 200

    time.sleep(3)

    # Check if the majority of the image is too dark or too bright
    if average_brightness < dark_threshold:
        return "The color is too dark"
    elif average_brightness > bright_threshold:
        return "The color is too bright"
    else:
        return "Good"

def main():
    st.title("Is the Color Okay?")
    st.caption('*\"Is the color okay?\"*')
    st.caption('*\"I dunno, ask this website!\"*')
    st.divider()

    with st.expander("See explanation"):
        st.text("""
                
                1. Please enable your camera
                2. No picture is saved
    
        """)

    uploaded_file = st.camera_input(" ")

    if uploaded_file is not None:

        # Convert the uploaded file to an OpenCV image
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        
        with st.spinner('🤖 : *Hmm is this color okay..?*'):
            result = analyze_image(image_np)

        st.subheader(f"Result: {result}")


if __name__ == "__main__":
    main()
