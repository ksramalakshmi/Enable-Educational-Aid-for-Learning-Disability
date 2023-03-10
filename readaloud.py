import pyttsx3
import time
import openai
import streamlit as st

openai.api_key = "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"

def read_aloud():
    st.title("Read Aloud With Me!")

    if st.button("Read Aloud", key='submit'):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        if st.button("Stop"):
            engine.stop()

        report = []
        res_box = st.empty()
        for resp in openai.Completion.create(model='text-davinci-003',
                                            prompt="Please give me a sample paragraph to read aloud by a child",
                                            max_tokens=120, 
                                            temperature = 0.5,
                                            stream = True):
            
            report.append(resp.choices[0].text)
            result1 = "".join(report[:-1]).strip()
            result2 = report[-1]
            result1 = result1.replace("\n", "")
            res_box.markdown(f'*{result1}* **:red[{result2}]**')
            engine.say(resp.choices[0].text)
            engine.runAndWait()
            