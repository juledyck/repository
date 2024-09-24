import streamlit as st
import time
import random
from streamlit_extras.let_it_rain import rain


def whem():
    rain(
        emoji="🥸",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

def herzchen():
    rain(
        emoji="🥰",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

def sleep():
    rain(
        emoji="😴",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

# Hauptbereich der Streamlit-App
st.title("Arnes Mini Gadged (Work in progress)")

# Erstelle einen Button
if st.button("Press Button luv"):

    herzchen()
    st.error("Ich hab dich ganz doll lieb!")

# Button 2
if st.button("Press Whem Button"):
    # Knopf verschwindet
    st.session_state.button_pressed = True

    whem()
    st.info("Cheer up! Deine Whem freut sich auf dich!")

# Button 3 
if st.button("Press Sleep Button"):
    # Knopf verschwindet
    st.session_state.button_pressed = True

    sleep()
    st.success("Gutschein für eine extra lange Massage vor dem schlafen.")