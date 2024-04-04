'''
Go to youtube and automatically find the most popular 
video of the day and return a youtube link and view count, 
possibly later on add the ability to scrape multiple websites 
and dump out (etc, reddit, tiktok, X).
'''


import requests
from bs4 import BeautifulSoup
from viral_finder import get_config

#get user input, this will change to arg passing at some point. 

YT_KEY = get_config()
TOP_VID_API = f"https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&maxResults=1&key={YT_KEY}"
response = requests.get(TOP_VID_API).json()
yt_vid_id = response['items'][0]['id']
vid_stat_api = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={yt_vid_id}&key={YT_KEY}"
response = requests.get(vid_stat_api).json()
viewcount = response['items'][0]['statistics']['likeCount']

print(f"URL: https://www.youtube.com/watch?v={yt_vid_id} \nViews: {viewcount}") 

