import streamlit as st
from tensorflow.keras.models import load_model
# from flower_classification_model import flowers
import pandas as pd
import cv2
import numpy as np

flowers = ['tulip', 'orchids', 'peonies', 'hydrangeas', 'lilies', 'gardenias', 'garden_roses', 'daisies', 'hibiscus', 'bougainvillea','sunflower', 'marigold', 'lavender', 'chrysanthemum', 'lotus', 'frangipani','jasmine', 'ixora','lantana','snapdragon']


# Load the trained model
model = load_model(r"C:\Users\Shureem Shokri\Documents\DEGREE\YEAR 3\SEM 2\FYP\code\flower_classification_model_latest")


# Function to preprocess a single image for prediction
def preprocess_single_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (256, 256))  # Resize the image to desired dimensions
    image = image / 255.0  # Normalize the image
    return image


# Function to predict the class of a single image
def predict_image_class(image):
    preprocessed_image = preprocess_single_image(image)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
    prediction = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(prediction)
    predicted_class = flowers[predicted_class_index]
    return predicted_class

#funtion to predict top 5 classes 
def predict_top5_classes(model, image, flowers):
    # preprocessed_image = preprocess_single_image(image_path)
    # prediction = model.predict(preprocessed_image)

    # # Get indices of top 5 predicted classes
    # top5_idx = np.argsort(prediction[0])[::-1][:5]

    # # Get the corresponding classes and percentages
    # top5_classes = [flowers[i] for i in top5_idx]
    # top5_percentages = [prediction[0][i] * 100 for i in top5_idx]

    # return top5_classes, top5_percentages
    
    preprocessed_image = preprocess_single_image(image)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
    prediction = model.predict(preprocessed_image)

    # Get indices of top 5 predicted classes
    top5_idx = np.argsort(prediction[0])[::-1][:5]

    # Get the corresponding classes and percentages
    top5_classes = [flowers[i] for i in top5_idx]
    top5_percentages = [prediction[0][i] * 100 for i in top5_idx]

    return top5_classes, top5_percentages

def classify_page():
    st.title("Classification 🌻🌼🌺🌹")
    st.subheader("This page is for you to try our image identifier!")
    
    st.title("Let's Start with The Image Classification!")
    st.subheader("Please follow this easy steps to start:-")
    st.subheader("1. Upload your image of flower in the required box.")
    st.subheader("2. Please wait for a few seconds for the model to predict the image.")
    
    uploaded_file = st.file_uploader("Please upload an image:", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Make a prediction
        # predicted_class = predict_image_class(image)
         # Make a prediction
        classes,percentage = predict_top5_classes(model, image, flowers)
        
        # # Show the predicted class
        # st.write("Thank you for uploading an image!\n The predicted class of the flower is:", predicted_class)
        st.write("Thank you for uploading an image!\n The predicted classes and percentages are:")
        # for i in range(5):
        #     st.write(f"{classes[i]}: {percentage[i]:.2f}%")

        # Display percentage graphs
        st.subheader("Percentage Graphs:")
        percentage_data = {"Class": classes, "Percentage": percentage}
        percentage_df = pd.DataFrame(percentage_data)
        st.bar_chart(percentage_df.set_index("Class"))  # Directly pass the DataFrame to st.bar_chart


# if __name__ == "__main__":
#     main()