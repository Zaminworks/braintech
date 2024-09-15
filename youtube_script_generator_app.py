import streamlit as st
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyA-HqP55k6H8d0yQ3_HGQXAQdY20qbfbxw")

# Set the generation configuration for the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 4096,
    "response_mime_type": "text/plain",
}

# Function to generate YouTube video script using Google Generative AI
def generate_video_script(topic):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])
    
    # Send the message with the user-provided topic
    message = f"Generate a detailed YouTube video script for the topic '{topic}'. The script should include an engaging introduction, a well-structured body with key points, and a compelling conclusion. It should be around 10 minutes long and formatted for a YouTube video."
    response = chat_session.send_message(message)
    
    # Return the generated text (video script)
    return response.text

# Streamlit Frontend

# Set up the Streamlit UI
st.title("AI-Powered YouTube Video Script Generator")

# Input box for the user to provide a topic
topic = st.text_input("Enter the topic for which you want to generate a YouTube video script:")

# Button to trigger video script generation
if st.button("Generate Video Script"):
    if topic:
        with st.spinner("Generating your video script..."):
            video_script = generate_video_script(topic)
            st.subheader("Generated YouTube Video Script")
            st.write(video_script)
    else:
        st.warning("Please enter a topic before generating.")
