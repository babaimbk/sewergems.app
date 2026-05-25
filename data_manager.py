import json
import os

def load_json(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

NOTES_FILE = "data/notes.json"
PROGRESS_FILE = "data/progress.json"
BOOKMARK_FILE = "data/bookmarks.json"

def get_notes():
    return load_json(NOTES_FILE)

def save_note(video_id, note):
    data = load_json(NOTES_FILE)
    data[video_id] = note
    save_json(NOTES_FILE, data)

def get_progress():
    return load_json(PROGRESS_FILE)

def save_progress(video_id, status):
    data = load_json(PROGRESS_FILE)
    data[video_id] = status
    save_json(PROGRESS_FILE, data)

def get_bookmarks():
    return load_json(BOOKMARK_FILE)

def toggle_bookmark(video_id):
    data = load_json(BOOKMARK_FILE)

    if video_id in data:
        del data[video_id]
    else:
        data[video_id] = True

    save_json(BOOKMARK_FILE, data)
