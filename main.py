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

def searchReddit(r, query):
    
    print("Fetching posts about " + query + "...")
    posts = r.subreddit("all").search([query], limit=50)    

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

    # # tester to print out specific search results in console, can be removed
    # if (query == "talk with AI Priest"):
    #     print("\n--- 50 Posts About talk with Guru ---")
    #     for i,posts in enumerate(posts_data, 1):
    #         print(f"\nPost {i}:")
    #         print(f"Title: {posts['title']}")
    #         print(f"Score: {posts['score']}")
    #         print(f"URL: {posts['url']}")
    #         print(f"Number of Comments: {posts['num_comments']}")
    #         print(f"Created: {posts['created']}")
    #         print(f"Body: {posts['body']}")
        
    
    return posts_data


if __name__ == "__main__":
    #different search terms involving AI and religion
    #could add searches or alter the search however you like
    search1 = searchReddit(reddit, "AI Jesus")
    search2 = searchReddit(reddit, "#ReligiousAI")
    search3 = searchReddit(reddit, "Christian AI chatbot")
    search4 = searchReddit(reddit, "TALKWITHAIRABBI")
    search5 = searchReddit(reddit, "talk with AI Muhammed")
    search6 = searchReddit(reddit, "AI Priest")
    
    # Save to CSV
    print("Saving posts to CSV...")
    with open('reddit_outputs.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=search1[0].keys())
        writer.writeheader()
        writer.writerows(search1)
        writer.writerows(search2)
        writer.writerows(search3)
        writer.writerows(search4)
        writer.writerows(search5)
        writer.writerows(search6)
        
    print("CSV saved successfully!")

        


