
### Reddit post collector
# This script collects posts from Reddit based on a search query, removes duplicates, and saves the results to a CSV file.
import datetime 
import praw
import csv
from textblob import TextBlob



reddit = praw.Reddit(
       client_id="right below: personal use script...",
       client_secret="yourSecretHere",
       password="yourPasswordHere",
       user_agent="script:dog_post_collector:v1.0 (by /u/username)",
       username="yourUsernameHere",
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
    
    ## Minor data engineering
    # Remove duplicates based on post id
    unique_posts = {}
    for post in all_posts:
        unique_posts[post['post_id']] = post
    
    # Convert back to list
    unique_posts_list = list(unique_posts.values())
    
    print("Collected " + str(len(all_posts)) + " total posts")
    print("After removing duplicates: " + str(len(unique_posts_list)) + " unique posts")
    
    for post in unique_posts_list:
    # Convert Unix timestamp to readable date(got this from claude)
        timestamp = datetime.datetime.fromtimestamp(post['created'])
        post['timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
    sorted_times = sorted(unique_posts_list, key=lambda x: x['created'])
    
    # Get earliest and latest dates
    earliest_date = datetime.datetime.fromtimestamp(sorted_times[0]['created']).strftime('%Y-%m-%d')
    latest_date = datetime.datetime.fromtimestamp(sorted_times[-1]['created']).strftime('%Y-%m-%d')
    
    print("Date range: " + str(earliest_date) + " to " + str(latest_date))
    
    # Sentiment analysis per post
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    for post in unique_posts_list:
        sentiment = TextBlob(post['title'] + " " + post['body_text']).sentiment.polarity
        if sentiment > 0.2:
            post['basic_sentiment'] = 'positive: ' + str(sentiment)
            positive_count += 1
        elif sentiment < -0.2:
            post['basic_sentiment'] = 'negative: ' + str(sentiment)
            negative_count += 1
        else:
            post['basic_sentiment'] = 'neutral: ' + str(sentiment)
            neutral_count += 1
    
    print("Sentiment analysis complete")
    print("Positive posts: " + str(positive_count))
    print("Negative posts: " + str(negative_count))
    print("Neutral posts: " + str(neutral_count))
    
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
       
    # Combine all posts into one text file
    all_posts_text = ""
    for post in unique_posts_list:
        all_posts_text += post['title'] + " " + post['body_text'] + " "
        
    print("All posts combined into one text file")
    with open('reddit_outputs.txt', 'w', encoding='utf-8') as f:
        f.write(all_posts_text)
        print("Text file saved successfully")
    
    # Calculate word frequencies
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
    
    print("All tasks complete")