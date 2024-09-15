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

# Function to generate blog titles using Google Generative AI
def generate_blog_titles(topic):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])
    
    # Send the message with the user-provided topic
    message = f"Generate 5 catchy and creative blog titles for the topic '{topic}'."
    response = chat_session.send_message(message)
    
    # Return the generated text (blog titles)
    return response.text

# Streamlit Frontend

# Set up the Streamlit UI
st.title("Blog Title Generator")

# Input box for the user to provide a topic
topic = st.text_input("Enter the topic for which you want to generate blog titles:")

# Button to trigger blog title generation
if st.button("Generate Blog Titles"):
    if topic:
        with st.spinner("Generating your blog titles..."):
            blog_titles = generate_blog_titles(topic)
            st.subheader("Generated Blog Titles")
            st.write(blog_titles)
    else:
        st.warning("Please enter a topic before generating.")
