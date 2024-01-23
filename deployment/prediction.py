import streamlit as st
import numpy as np
import tensorflow as tf
from io import BytesIO
from keras.models import load_model


# Load model
model = load_model('model.h5')


# Setup the webpage
def run():
    
    st.write('# What kind of vehicle is this?')
    st.write('##### Test the object detection model')

    
    file = st.file_uploader('Upload an image of a vehicle', type=['png', 'jpg'])
    show_file = st.empty()
        
    if not file:
        show_file.info('Upload an image of any military vehicle here. Allows png and jpg. \
                       Press *Detect* to let the model guess. Pressing *Detect* without any image \
                       uploaded will yield an error.')
    else:
        content = file.getvalue()

    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        print('File must be an image') 

        # Submit image button
    with st.form('vehicleDetection'):          
        guess = st.form_submit_button('Detect')

    # When the Detect button is pressed
    if guess:
        img = tf.keras.utils.load_img(file, target_size=(150, 150))
        x = tf.keras.utils.img_to_array(img)/255


        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        idx = np.argmax(classes)
        clas = ['Anti-aircraft','Armored combat support vehicles','Armored personnel carriers',
          'Infantry fighting vehicles','Light armored vehicles','Mine-protected vehicles',
          'Prime movers and trucks', 'Self-propelled artillery', 'light utility vehicles',
          'tanks']
        st.write('This is a {}'.format(clas[idx])) 



if __name__ == '__main__':
    run()
