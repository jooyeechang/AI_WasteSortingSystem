import streamlit as st
from PIL import Image
import os

# Streamlit app setup
st.title("AI Waste Sorting Chatbot")
st.write("""
    This chatbot helps you determine whether an item is recyclable, provides recycling options, 
    and gives nearby recycling center suggestions.
""")

# Set up the API key using environment variable
my_secret = os.environ['Gemini_key']  # Ensure this key is correctly set in your environment

# Upload the image
uploaded_file = st.file_uploader("Upload a photo of the waste item", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Waste Item", use_column_width=True)

    # Ensure the API is set up properly and import the library inside the function
    import google.generativeai as genai
    genai.configure(api_key=my_secret)  # Configure the API with the secret key

    # Base AI Chatbot setup
    AI_Chatbot = genai.GenerativeModel("gemini-1.5-flash",
        system_instruction="""
            You are an AI expert in waste management, recycling, and reusing. 
            You analyze uploaded photos to:
            1) Recommend if the item is recyclable or not.
            2) Categorize the waste and suggest recycling methods, especially for electronic devices.
            3) Suggest nearby recycling centers (with user permission).
            4) Provide estimated prices for recyclable materials in MYR.
        """
    )

    # Generate response
    if st.button("Analyze Waste Item"):
        with st.spinner("Analyzing the waste..."):
            # Sending the image to the AI model for analysis (adjust this based on how the API expects the image)
            response = AI_Chatbot.generate_content(['Here is an image:', img])

        # Output the chatbot response
        st.write(response.text)

# Footer
st.write("Powered by Google Generative AI")
