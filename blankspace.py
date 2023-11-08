import os
import json
from googleapiclient.discovery import build

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # DO NOT leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDsMwmQeItUE4T4Stzq6mYTxelrdOaUL_8"

    youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=300,
        videoId="gir8BEqAutk"
    )
        # Execute the API request and get the response
    response = request.execute()

    # Load existing comments from the JSON file (if it exists)
    existing_comments = []
    if os.path.isfile('youtube_comments.json'):
        with open('youtube_comments.json', 'r') as json_file:
            existing_comments = json.load(json_file)

    # Append new comments to the existing list
    existing_comments.extend(response['items'])

    # Save the combined comments to the JSON file
    with open('youtube_comments.json', 'w') as json_file:
        json.dump(existing_comments, json_file, indent=4)

    return response

# Run your main function to fetch and append new comments

if __name__ == "__main__":
    main()