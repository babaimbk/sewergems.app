import streamlit as st
import json
from utils.data_manager import *
from utils.ui_components import *

PLAYLIST_ID = "PLLCOESNdmKSIcI0SgyiBipZdCXm1T_F9_"
PLAYLIST_URL = f"https://www.youtube.com/playlist?list={PLAYLIST_ID}"

st.set_page_config(layout="wide", page_title="SewerGEMS Learning")

# -----------------------------
# LOAD DATA
# -----------------------------
with open("data/topics.json") as f:
    topics = json.load(f)

notes = get_notes()
progress = get_progress()
bookmarks = get_bookmarks()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🎛️ Controls")

search = st.sidebar.text_input("Search Topic")

view_mode = st.sidebar.radio(
    "View Mode",
    ["Topic Mode", "Playlist Mode"]
)

show_bookmarks = st.sidebar.checkbox("⭐ Bookmarked Only")

filtered = topics

if search:
    filtered = [t for t in filtered if search.lower() in t["title"].lower()]

if show_bookmarks:
    filtered = [t for t in filtered if t["video_id"] in bookmarks]

titles = [t["title"] for t in filtered]

selected_title = st.sidebar.radio("Select Topic", titles)

selected = next(t for t in topics if t["title"] == selected_title)
vid = selected["video_id"]

st.sidebar.markdown("---")
st.sidebar.link_button("🔗 Open Full Playlist", PLAYLIST_URL)

# -----------------------------
# MAIN LAYOUT
# -----------------------------
col1, col2 = st.columns([1, 2])

# -----------------------------
# LEFT PANEL
# -----------------------------
with col1:
    st.header("📚 Topics")

    for t in filtered:
        topic_card(
            t["title"],
            selected=(t["title"] == selected_title)
        )

# -----------------------------
# RIGHT PANEL
# -----------------------------
with col2:
    st.header("🎥 Learning Panel")

    if view_mode == "Topic Mode":
        video_player(vid)
    else:
        playlist_player(PLAYLIST_ID)

    st.subheader(selected["title"])

    # BOOKMARK
    if st.button("⭐ Toggle Bookmark"):
        toggle_bookmark(vid)
        st.success("Updated")

    # PROGRESS
    completed = st.checkbox(
        "✅ Completed",
        value=progress.get(vid, False)
    )
    save_progress(vid, completed)

    # NOTES
    st.subheader("📝 Notes")

    note = st.text_area(
        "Write notes",
        value=notes.get(vid, ""),
        height=150
    )

    if st.button("💾 Save Note"):
        save_note(vid, note)
        st.success("Saved")

    # PLAYLIST BUTTON
    st.markdown("### 🔗 Full Playlist")
    st.link_button("Open Playlist", PLAYLIST_URL)

# -----------------------------
# ROADMAP
# -----------------------------
st.markdown("---")
st.header("🗺️ Roadmap")

for t in topics:
    status = "✅" if progress.get(t["video_id"]) else "⬜"
    mark = "⭐" if t["video_id"] in bookmarks else ""
    st.write(f"{status} {mark} {t['title']}")
