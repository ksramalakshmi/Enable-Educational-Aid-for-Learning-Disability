import streamlit as st
import learn
import summary
import readaloud
import jago

def main():
    st.set_page_config(
        page_title="Enable Educational Aid",
        page_icon=":books:",
    )
    st.title("Enable Educational Aid")
    st.subheader("A tool to help you learn your lessons")

    feature_menu = ["Choose what you want to do!", "Learn English Lessons!", "Read aloud with me!", "Meet your companion Jago!"]

    feature_choice = st.sidebar.selectbox("It's study time!", feature_menu)
    match feature_choice:
        case "Learn English Lessons!":
            learn.learn_page()
        case "Read aloud with me!":
            readaloud.read_aloud()
        case "Meet your companion Jago!":
            jago.jagochat()


if __name__ == '__main__':
    main()