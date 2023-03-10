import streamlit as st
import learn
import summary

def main():
    st.set_page_config(
        page_title="Enable Educational Aid",
        page_icon=":books:",
    )
    st.title("Enable Educational Aid")
    st.subheader("A tool to help you learn your lessons!")

    # page_bg_img = '''
    # <style>
    # body {
    # background-image: url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
    # background-size: cover;
    # }
    # </style>
    # '''

    # st.markdown(page_bg_img, unsafe_allow_html=True)
    

    feature_menu = ["Choose what you want to do!", "Learn English Lessons!", "Quiz Yourself!", "Summarise Lesson!"]

    feature_choice = st.sidebar.selectbox("It's study time!", feature_menu)
    match feature_choice:
        case "Learn English Lessons!":
            learn.learn_page()
        case "Quiz Yourself!":
            st.write("Quiz Yourself!")
        case "Summarise Lesson!":
            summary.summarise()

if __name__ == '__main__':
    main()