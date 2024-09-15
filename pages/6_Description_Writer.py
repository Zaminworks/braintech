import streamlit as st
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyA-HqP55k6H8d0yQ3_HGQXAQdY20qbfbxw")

# Set the generation configuration for the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

# Function to generate YouTube video description using Google Generative AI
def generate_video_description(topic):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])
    
    # Send the message with the user-provided topic
    message = f"Generate an engaging and SEO-optimized YouTube video description for the topic '{topic}'. The description should be informative, include relevant keywords, and encourage viewers to like, comment, and subscribe."
    response = chat_session.send_message(message)
    
    # Return the generated text (video description)
    return response.text

# Streamlit Frontend

# Set up the Streamlit UI
st.title("AI-Powered YouTube Video Description Generator")

# Input box for the user to provide a topic
topic = st.text_input("Enter the topic for which you want to generate a YouTube video description:")

# Button to trigger video description generation
if st.button("Generate Video Description"):
    if topic:
        with st.spinner("Generating your video description..."):
            video_description = generate_video_description(topic)
            st.subheader("Generated YouTube Video Description")
            st.write(video_description)
    else:
        st.warning("Please enter a topic before generating.")
