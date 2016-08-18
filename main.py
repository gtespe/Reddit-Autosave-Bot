#!/usr/bin/python
import praw

# Connect to Reddit
user_agent = "Title Searching bot 1.0 by /u/titlesearchbot"
reddit = praw.Reddit(user_agent=user_agent)
reddit.login(disable_warning=True)
subreddit = reddit.get_subreddit(input("Enter a Subreddit:\n>> r/"))

found_posts = []

#Enter Search terms, turns a string into a list of strings
search_terms = []
search_terms = (input("Enter Search Terms (Separated by spaces)") + " ").split()

print ("searching for " + str(search_terms))

# Start searching for new posts
while True:
    # Get first 20 posts
    for post in subreddit.get_new(limit=50):  
        # cycle through terms
        for term in search_terms:
            # check if the post is not already indexed and contains the term
            if post not in found_posts and term in str(post):
                # append it to the found_posts list and save it to your profile
                found_posts.append(post)
                post.save()
                break
            
            
