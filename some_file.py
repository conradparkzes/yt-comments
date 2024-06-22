# pip install --upgrade google-api-python-client
# use above for client import

import googleapiclient.discovery
import requests
import pandas as pd
import sqlalchemy as db


def comment_threads(video_id):
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = 'AIzaSyC7DYYMBkl50jZ-oiAlPZJ8W2Z3neOyTtU'

    youtube = googleapiclient.discovery.build(api_service_name, api_version, 
    developerKey = DEVELOPER_KEY)
    request = youtube.commentThreads().list(part='snippet',videoId=video_id,
    maxResults=10,order='relevance')
    response = request.execute()

    return response

video_id = 'WEmcW59Hz6M'
comments = comment_threads(video_id)

i = 1 # iterative for id
c = {} 

for item in comments['items']:
    date = item['snippet']['topLevelComment']['snippet']['publishedAt']
    c[i] = (item['snippet']['topLevelComment']['snippet']['authorDisplayName']),(item['snippet']['topLevelComment']['snippet']['textDisplay']),(item['snippet']['topLevelComment']['snippet']['likeCount']),(date[(date.find('2')):(date.find('T'))])
    i+=1

dataframe = pd.DataFrame.from_dict(c)

engine = db.create_engine('sqlite:///topcomments.db')

dataframe.to_sql('topCommentsTable', con=engine, if_exists='replace',index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM topCommentsTable;")).fetchall()
    print(pd.DataFrame(query_result))