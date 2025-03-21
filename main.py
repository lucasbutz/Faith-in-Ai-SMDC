#Meta App ID: 3814003358929786
#import requests
# ACCESS_TOKEN = "EAA2M0Nthk3oBO3PingP1UMZBLhgclWf9yBWl4iVcBPQnX3fcxQMWiTyFlEqGHsobCg3pVCOitQ5UYdRZAHtZBjqDZBSf3K91GFwA4H0wPd8KPtRxpb2IlCfvPsJYDbcTm7dUaEaZCOjndf5ztz2VkVamtRs1ZBUYHZBb2UHyyZBUN9I9O0hZAZBJ4cXEzcXU08bvbBVWt41pErm1Blsk5rJflVZB8dPN6Bmc0vfDzKy0OyS87eZBZAaPQ6AGkUNqczf5612i3RFCcmAZDZD"


## Reddit API
import praw
import csv
#import json
#from pprint import pprint


reddit = praw.Reddit(
        client_id="gY3V4lnTMRgiXXD8P24arA",
        client_secret="w6wPh1jbJhKl8V21DTxAnLtsHvs9Ew",
        password="Pollution@3",
        user_agent="script:dog_post_collector:v1.0 (by /u/CryptographerOne6528)",
        username="CryptographerOne6528",
    )

def searchAIJesus(red):
    print("Connecting to Reddit API...")
    
    # Initialize the Reddit instance with your credentials
    r = red
    print("Successfully authenticated!")
    # Search for posts about AI Jesus

    print("Fetching 5 posts about AI Jesus...")
    posts = r.subreddit("all").search("AI Jesus", limit=5)    

    posts_data = []
    for post in posts:
        posts_data.append({
        'title': post.title,
        'score': post.score,
        'id': post.id,
        'url': post.url,
        'num_comments': post.num_comments,
        'created': post.created_utc,
        'body': post.selftext

        })

    for i,posts in enumerate(posts_data, 1):
        print(f"\nPost {i}:")
        print(f"Title: {posts['title']}")
        print(f"Score: {posts['score']}")
        print(f"URL: {posts['url']}")
        print(f"Number of Comments: {posts['num_comments']}")
        print(f"Created: {posts['created']}")
        print(f"Body: {posts['body']}")
        
    
    return posts_data
    
    # # Print post details
    # print("\n--- 5 Posts About AI Jesus ---")
    # for i, post in enumerate(dog_posts, 1):
    #     print(f"\nPost {i}:")
    #     print(f"Title: {post.title}")
    #     print(f"Subreddit: r/{post.subreddit.display_name}")
    #     print(f"Score: {post.score}")
    #     print(f"URL: https://reddit.com{post.permalink}")

    # print("\nAPI test completed successfully!")

if __name__ == "__main__":
    search1 = searchAIJesus(reddit)
    
    # Save to CSV
    print("Saving posts to CSV...")
    with open('reddit_ai_jesus.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=search1[0].keys())
        writer.writeheader()
        writer.writerows(search1)


