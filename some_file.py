import googleapiclient.discovery
import requests
import pprint
import json

def comment_threads(video_id):
  api_service_name = 'youtube'
  api_version = 'v3'
  DEVELOPER_KEY = 'AIzaSyC7DYYMBkl50jZ-oiAlPZJ8W2Z3neOyTtU'

  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
  request = youtube.commentThreads().list(part='snippet',videoId=video_id,maxResults=10)#,order='relevance')
  response = request.execute()

  return response

video_id = 'WEmcW59Hz6M'
comments = comment_threads(video_id)
# pprint.pprint(comments)
# print(comments)

# print(type(comments))
# for comment in comments:
  # print(type(comment))
  # print(comment['items']['snippet']['topLevelComment']['snippet']['textDisplay'])


print('The most recent comments on the video, \"Mbappé is Good but... Messi & Ronaldo were Monsters at 19!\":')
print()
i = 1
for item in comments['items']:
  c = item['snippet']['topLevelComment']['snippet']['textDisplay']
  print(f'{i}. {c}')
  i+=1
