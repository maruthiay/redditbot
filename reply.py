import praw
import prawcore
import time

reddit = praw.Reddit('MchanBot')


#Checks the file with links to harmful messages
#Comments on harmful messages with a reminder to treat others with respect
f = open('CommentPermalinks1.txt', 'r+')
linksList = f.read().strip().split('\n')
for link in linksList:
    url = "https://www.reddit.com" + str(link)
    submission = reddit.submission(url=url)
    #print(comment)
    submission.reply('Please be polite, Cyber Bullying is against the rules of this Forum') ###CHANGE MESSAGE

f.close()


