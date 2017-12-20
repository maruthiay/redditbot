#!/usr/bin/python
import praw

reddit = praw.Reddit('MchanBot')

subreddit = reddit.subreddit("all")

#open files to record data
presentReference = open("PresentDataReference.txt","r+")
notPresentReference = open("NotPresentDataReference.txt","r+")
present = open("PresentData.txt","r+")
notPresent = open("NotPresentData.txt","r+")

for submission in subreddit.hot(limit=5):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if all(ord(c) < 128 for c in comment.body):
            presentReference.write('\n'+comment.body +'\n'+'-----')
            present.write(comment.body+'-----')


#closes files
present.close()
notPresent.close()
presentReference.close()
notPresentReference.close()

