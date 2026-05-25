from googleapiclient.discovery import build
import json
import os

API_KEY = "YOUR_YOUTUBE_API_KEY"
PLAYLIST_ID = "PLLCOESNdmKSIcI0SgyiBipZdCXm1T_F9_"

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_all_videos():
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=PLAYLIST_ID,
            maxResults=50,
            pageToken=next_page_token
        )

        response = request.execute()

        for item in response["items"]:
            videos.append({
                "title": item["snippet"]["title"],
                "video_id": item["snippet"]["resourceId"]["videoId"]
            })

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return videos

os.makedirs("data", exist_ok=True)

videos = get_all_videos()

with open("data/topics.json", "w") as f:
    json.dump(videos, f, indent=4)

print("✅ topics.json created with REAL video IDs")
``
