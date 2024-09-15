import streamlit as st
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyA-HqP55k6H8d0yQ3_HGQXAQdY20qbfbxw")

# Set the generation configuration for the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Function to generate a blog post using Google Generative AI
def generate_blog_post(topic):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )
    
    # Start a chat session with an empty history
    chat_session = model.start_chat(history=[])
    
    # Send the message with the user-provided topic
    message = f"Write a detailed blog post on {topic} which is 100% SEO optimized. Make it human-written and give some tags and hashtags related to the topic to improve SEO."
    response = chat_session.send_message(message)
    
    # Return the generated text
    return response.text

# Streamlit Frontend

# Set up the Streamlit UI
st.title("SEO Optimized Blog Post Generator")

# Input box for the user to provide a blog topic
topic = st.text_input("Enter the topic for the blog post:")

# Button to trigger blog post generation
if st.button("Generate Blog Post"):
    if topic:
        with st.spinner("Generating your blog post..."):
            blog_post = generate_blog_post(topic)
            st.subheader("Generated Blog Post")
            st.write(blog_post)
    else:
        st.warning("Please enter a topic before generating.")
