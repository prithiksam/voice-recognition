import streamlit as st
import speech_recognition as sr
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Say something...")
        audio = recognizer.listen(source)

    try:
        st.success("Recognizing...")
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        st.error("Oops! Couldn't understand the audio.")
    except sr.RequestError as e:
        st.error(f"Error connecting to the Google API: {e}")
    except Exception as e:
        st.error(f"Error: {e}")
def main():
    st.title("Voice Recognition in Streamlit")

    # Voice Recognition Button
    if st.button("Start Voice Recognition"):
        recognized_text = recognize_speech()
        if recognized_text:
            st.subheader("Recognized Text:")
            st.write(recognized_text)

if __name__ == "__main__":
    main()
