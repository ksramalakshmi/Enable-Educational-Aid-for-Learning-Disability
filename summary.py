import openai
import streamlit as st

openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt="Please summarize this in a few sentences: "+prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def summarise():

    st.title("Enable Summarizer")

    prompt = st.text_area("Enter your message:", key='prompt')
    if st.button("Submit", key='submit'):
        response = generate_response(prompt)
        st.success(response)