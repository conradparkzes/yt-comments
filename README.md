# yt-comments
![workflow badge](https://github.com/conradparkzes/yt-comments/actions/workflows/style.yaml/badge.svg)
### Setup instructions
* install libraries: googleapiclient with discovery module, requests, pandas, 
sqlalchemy
* developer key for access to YouTube API is necessary

### How to run the code (not accurate, but ideally)
Running the program will ask you for a user input of the video ID of a YouTube
video of your choice. This ID can be found at the end of a general url link, 
bounded by the "=" and "&" symbols to your desired YouTube video. Input 
this ID, and returned will be information about the top comments on the 
selected video.

 ### Code overview
The code stores all available data from the CommentsThread tool of the 
YouTube API in a dictionary, that is then accessed by certain key names to
pull out username, comment text, like count, and date of comment.
Data is then stored in a Pandas DataFrame, and converted to a SQL table.