import streamlit as st

def video_player(video_id):
    url = f"https://www.youtube.com/embed/{video_id}"
    st.components.v1.iframe(url, height=450)

def playlist_player(playlist_id):
    url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
    st.components.v1.iframe(url, height=450)

def topic_card(title, selected=False):
    if selected:
        st.success(title)
    else:
        st.write(title)
``
