import praw
import json

#public: ZhjWeAKJ0wg9rHZ3GkeW1A
#private: 8Cd1ZHplMMmR6OTqIXj-5mwIaCCItw

#reddit is a very interesting 



#of course, just running this from the source code probably isnt going to work for
#any student, unless they include their private api key... this is just data scraping though


##### Other code happens in NetworkGraphFactory.py #####

#This grabs me the "user" objects for the top 10 comments on the top 25 hottest posts on the front
#page of reddit. This leaves me with a total of 250 individuals. For those indiviudals, I scraped
#their most recent 50 comments (or however many up till that point that they have) and notes
#the subreddit that they commented in. The results of this can be seen in my 4500+ line JSON
#file, Redditors.JSON

#This network graph worked better than I could possibly imagine. If youre a reddit person, 
#I would reccomend running the network graph with 40, 30, 20, 15, 10, 8 and below
#The graph turned out well, and looking at the individual subreddits (and which ones are connected) is
#quite entertaining.

#connections like "r/kermitthefrog" attached to "r/millionairemakers"
#and lots of things like that. I especially liked "programmeradvice"
#connected to "cryptocurrency" connected to "life advice"...apparently
#bad programmers put too much money into crypto and are trying to figure out
#their lives. Incredible.

##### DATA SCRAPE START #####

reddit = praw.Reddit(
        client_id="ZhjWeAKJ0wg9rHZ3GkeW1A",
        client_secret="----SECRET ID HERE----",
        user_agent="Student_Python:v1.0.0",
        username="comenoha",
        password="----PASSWORD WOULD GO HERE----")

reddit_instance = []; #this will hold a list of all reddit users instances -> Redditors.csv

top_comments = 10;
num_subreddits = 25;

blacklist = ["AutoModerator", "unexBot", "QualityVote"]

for submission in reddit.subreddit("all").hot(limit=num_subreddits):
    
    index = 0
    added = 0
    
    while added < top_comments:
        
        try:
            auth = submission.comments[index].author
            
            if(auth in reddit_instance):
                print("SIMILAR COMMENTOR - kinda surprised")
            else:
                if(auth.name not in blacklist):
                    reddit_instance.append(auth)
                    print("ADDED: " + auth.name)
                    added = added + 1
                index = index + 1
        except:
            print("something happened here")
            index = index + 1
            
        
#run through user's individual comments and check which subreddits they are

top_comments_Redditor_data = {}


for user in reddit_instance:
    
    top_comments_Redditor = 50
    
    top_comments_Redditor_data_individual = {}
    
    comments = list(user.comments.new())
    
    if(len(comments) < top_comments_Redditor):
        top_comments_Redditor = len(comments) - 1
    
    for i in range(top_comments_Redditor):
        subreddit = comments[i].subreddit.display_name
        
        if(subreddit in top_comments_Redditor_data_individual):
            top_comments_Redditor_data_individual[subreddit] += 1
        else:
            top_comments_Redditor_data_individual[subreddit] = 1
    
    top_comments_Redditor_data[user.name] = top_comments_Redditor_data_individual

#I DO NOT WANNA DO THIS MULTIPLE TIMES
#SO ILL BE WRITING TO A JSON FOR THIS

with open("Redditors_JSON.json", "w") as output:
    json.dump(top_comments_Redditor_data, output, indent=4)
