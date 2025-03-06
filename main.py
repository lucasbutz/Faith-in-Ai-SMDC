#Meta App ID: 3814003358929786

#import requests

# ACCESS_TOKEN = "EAA2M0Nthk3oBO3PingP1UMZBLhgclWf9yBWl4iVcBPQnX3fcxQMWiTyFlEqGHsobCg3pVCOitQ5UYdRZAHtZBjqDZBSf3K91GFwA4H0wPd8KPtRxpb2IlCfvPsJYDbcTm7dUaEaZCOjndf5ztz2VkVamtRs1ZBUYHZBb2UHyyZBUN9I9O0hZAZBJ4cXEzcXU08bvbBVWt41pErm1Blsk5rJflVZB8dPN6Bmc0vfDzKy0OyS87eZBZAaPQ6AGkUNqczf5612i3RFCcmAZDZD"


## Reddit API
import praw
#import json
from pprint import pprint


def test_reddit_connection():
    print("Connecting to Reddit API...")
    
    # Initialize the Reddit instance with your credentials
    reddit = praw.Reddit(
        client_id="gY3V4lnTMRgiXXD8P24arA",
        client_secret="w6wPh1jbJhKl8V21DTxAnLtsHvs9Ew",
        password="Pollution@3",
        user_agent="script:dog_post_collector:v1.0 (by /u/CryptographerOne6528)",
        username="CryptographerOne6528",
    )
    
    print("Successfully authenticated!")
    # Search for posts about Dogs

    print("Fetching 5 posts about Dogs...")
    dog_posts = reddit.subreddit("all").search("planes", limit=5)    


    # Print post details
    print("\n--- 5 Posts About Dogs ---")
    for i, post in enumerate(dog_posts, 1):
        print(f"\nPost {i}:")
        print(f"Title: {post.title}")
        print(f"Subreddit: r/{post.subreddit.display_name}")
        print(f"Score: {post.score}")
        print(f"URL: https://reddit.com{post.permalink}")

    print("\nAPI test completed successfully!")

if __name__ == "__main__":
    test_reddit_connection()

