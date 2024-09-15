import streamlit as st
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyA-HqP55k6H8d0yQ3_HGQXAQdY20qbfbxw")

# Set the generation configuration for the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

# Function to generate tags and hashtags using Google Generative AI
def generate_tags(topic):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])
    
    # Send the message with the user-provided topic
    message = f"Generate 30 SEO tags related to the topic '{topic}' to improve SEO."
    response = chat_session.send_message(message)
    
    # Return the generated text (tags and hashtags)
    return response.text

# Streamlit Frontend

# Set up the Streamlit UI
st.title("SEO Tags Generator")

# Input box for the user to provide a topic
topic = st.text_input("Enter the topic for which you want SEO tags:")

# Button to trigger tags generation
if st.button("Generate Tags"):
    if topic:
        with st.spinner("Generating your SEO tags..."):
            tags_and_hashtags = generate_tags(topic)
            st.subheader("Generated SEO Tags")
            st.write(tags_and_hashtags)
    else:
        st.warning("Please enter a topic before generating.")
