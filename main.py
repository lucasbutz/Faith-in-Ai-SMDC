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
        'post_id': post.id,
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
    
    # Combine all search results
    all_posts = search1 + search2 + search3 + search4 + search5 + search6
    
    for post in all_posts:
        # make columns purpose clear
        post['body_text'] = post.pop('body')
    
    # Remove duplicates based on post id
    unique_posts = {}
    for post in all_posts:
        unique_posts[post['post_id']] = post
    
    # Convert back to list
    unique_posts_list = list(unique_posts.values())
    
    print("Collected " + str(len(all_posts)) + " total posts")
    print("After removing duplicates: " + str(len(unique_posts_list)) + " unique posts")
    
    # Save to CSV
    print("Saving posts to CSV...")
    with open('reddit_outputs.csv', mode='w', newline='', encoding='utf-8') as f:
        if unique_posts_list:
            writer = csv.DictWriter(f, fieldnames=unique_posts_list[0].keys())
            writer.writeheader()
            writer.writerows(unique_posts_list)
            print("CSV saved successfully")
        else:
            print("No posts found to save")
       
       
    all_posts_text = ""
    for post in unique_posts_list:
        all_posts_text += post['title'] + " " + post['body_text'] + " "
        
    print("All posts combined into one text file")
    with open('reddit_outputs.txt', 'w', encoding='utf-8') as f:
        f.write(all_posts_text)
        print("Text file saved successfully")
    
    word_freqencies = {}
    for word in all_posts_text.split():
        if word in word_freqencies:
            word_freqencies[word] += 1
        else:
            word_freqencies[word] = 1
        
    # Sort by frequency of words, hishest freq at top, will need to take out stop words later        
    sorted_x = sorted(word_freqencies.items(), key=lambda kv: kv[1])
    sorted_x.reverse()
    word_freqencies = dict(sorted_x)
            
    print("Word frequencies calculated")
    with open('word_frequencies.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Frequency"])
        for word, frequency in word_freqencies.items():
            writer.writerow([word, frequency])
        print("Word frequencies saved successfully")
    



