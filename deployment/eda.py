import streamlit as st
from PIL import Image

# Konfigurasi layout webpage
st.set_page_config(
    page_title = 'Military Vehicles Detector',
)

def run():

    # Title
    st.title('Military Vehicles Detector')

    # Sub-header
    st.subheader('CNN-based Object Detection Model Deployment to Detect Military Vehicles')

    # Image
    image = Image.open('t90ms.png')
    st.image(image, caption='Russian T90MS during training.')

    # Description
    st.write('This is a computer vision model deployment using Convolution Neural Network \
             The model is trained to detect ten categories of military vehicles: Anti-aircraft, \
             Armored combat support vehicles, Armored personnel carriers, Infantry fighting vehicles, \
             Light armored vehicles, Mine-protected vehicles, Prime movers and trucks, \
             Self-propelled artillery, light utility vehicles, and tanks. This is the display page. \
             User may upload an image on the prediction page to play around with the model. \
             Note that the image has to be 150 x 150 pixel in size.')


if __name__ == '__main__':
    run()
