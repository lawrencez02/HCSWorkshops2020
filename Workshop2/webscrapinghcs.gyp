import praw

reddit = praw.Reddit(client_id='eo0auD7DJitk-A', client_secret='8oDqhqgV7jerxUHNfUbJybbUYXg9QQ', user_agent='Reddit WebScraping')
hot_posts = reddit.subreddit('ApplyingToCollege').top(limit=100)
for post in hot_posts:
    print("Title: " + post.title)
    print("Body: " + post.selftext)
