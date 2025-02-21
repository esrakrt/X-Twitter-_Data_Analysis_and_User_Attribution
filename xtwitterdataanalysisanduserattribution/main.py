import json
from person import Person 
from person import person_info as info
from data_structures import *
import sys
from PyQt5.QtWidgets import QApplication
from graf_operations import Graph , GraphVisualizer,bfs
#from proje_3 import group_users_by_interest,print_interests
from ilgalanı import interests, same_users 
from frekans import en_cok_gecen_kelimeler


with open('twitter_data.json', 'r', encoding='utf-8') as file:
    twitter_data = json.load(file)

users = [None] * len(twitter_data)
user_table = HashTable()
users_tweets = HashTable()
users_graph = Graph()
str = ""
language = HashTable()
region = HashTable()

if __name__ == "__main__":
  
   
    for i in range(len(twitter_data)):
        #nesne olusturuyoruz 
        users[i]=info(
             Person(
            twitter_data[i]['username'],
            twitter_data[i]['name'],
            twitter_data[i]['followers_count'],
            twitter_data[i]['following_count'],
            twitter_data[i]['language'],
            twitter_data[i]['region']
        ),
            twitter_data[i]['tweets'],
            twitter_data[i]['followers'],
            twitter_data[i]['following']
        )
        
        tweets =myList()

        for j in range(len( twitter_data[i]['tweets'])):
             tweets.insert(twitter_data[i]['tweets'][j])


        tweets_str = " ".join(twitter_data[i]['tweets'])
        #str = " ".join(twitter_data[i]['tweets']) + str
        
        users_tweets.__setitem__(twitter_data[i]['username'],tweets)
        
       
         #hashable kullanıcılar için
        user_table.__setitem__(twitter_data[i]['username'], users[i])
       
        #tum kullanıcıların olduğu graph
        users_graph.addVertex(users[i].person.username,users[i])
    
     #tum kullanıcıların duğumlerini olusturduk sşimdi her birini gezip 
     #followers ve followinge gore edge elklencek     
     # fordan cıktık


    for user in users:
        interests(user,user.tweets)
    
    print(users[0].greet())
    same_users()
    
    sonuclar = {}
    sonuclar1 = {}
    for user_info in user_table.get_items():
        user = user_info[1].person
        if language.__getitem__(user.language) is None:
            language.__setitem__(user.language, users_tweets.__getitem__(user.username))
        #else:
       #     language.__getitem__(user.language).extend(users_tweets.__getitem__(user.username))
        if region.__getitem__(user.region) is None:
            region.__setitem__(user.region, users_tweets.__getitem__(user.username))
        #else:  #      region.__getitem__(user.region).extend(users_tweets.__getitem__(user.username))
    

             

    for key, item in region.get_items():
        tweets_str = " ".join([tweet for tweet in item])
        en_cok_gecen_re = en_cok_gecen_kelimeler(tweets_str, 5)
        sonuclar1[f"{key} bölgesindeki hashtag ler"] = [kelime for kelime, _ in en_cok_gecen_re]

    for key, item in language.get_items():
        tweets_str = " ".join([tweet for tweet in item])
        en_cok_gecen_la = en_cok_gecen_kelimeler(tweets_str, 5)
        sonuclar[f"{key} dilindeki hashtag ler"] = [kelime for kelime, _ in en_cok_gecen_la]

    with open('hashtagler.json', 'w',encoding = 'utf-8') as f:
        json.dump(sonuclar, f, ensure_ascii=False, indent=4)
    with open('hashtagler.json', 'a',encoding = 'utf-8') as f:
        json.dump(sonuclar1, f, ensure_ascii=False, indent=4)    


    name = input("graf icin kullanici adi girin: ")
    result = user_table.__getitem__(name)
    print(result)
    followers = result.followers  
    following = result.following  
    #followers = myList()
    #print(followers)
   
    show_graph = Graph()

    show_graph.addVertex(name,user_table.__getitem__(name))

    for follower in followers:
      
      show_graph.addVertex(follower,user_table.__getitem__(follower))
      show_graph.addEdge(follower, name) 

    for followed in following:
      show_graph.addVertex(followed,user_table.__getitem__(followed))
      show_graph.addEdge(name, followed)

    app = QApplication(sys.argv)
    window = GraphVisualizer(show_graph, followers, following)
    window.show()  
    print("show graf")
 
name1 = input("kullanici1 adi girin: ")  
name2 = input("kullanici2 adi girin: ")
result = user_table.__getitem__(name1)
followers1 = result.followers  
following1 = result.following 

is_follower = False
for follower in followers1:
  if name2 == follower:
    print(name2 + " " + name1 + " kisisinin takipcisi") 
    is_follower = True
if not is_follower:
    print(name2 + " " + name1 + " kisisinin takipcisi degil")

is_following = False
for followed in following1:
  if name2 == followed:
    print(name1 + " " + name2 + " kisisinin takipcisi") 
    is_following = True
if not is_following:
    print(name1 + " " + name2 + " kisisinin takipcisi degil")


#15 dk
#i=0
for user in users:
   # i = i + 1
   # print(f"i = {i}")
    result = user_table.__getitem__(user.person.username) 
    followers = result.followers  
    following = result.following
    for follower in followers:
        users_graph.addEdge(follower, result) 

    for followed in following: 
        users_graph.addEdge(result, followed)
print("user graf")     



print("in bfs")
same_followers = bfs(users_graph,users[0],user_table)
print("out of bfs")

results = {}
for followers_count, users in same_followers.get_items():
    users_str = " ".join(users)
    results[f"Followers Count: {followers_count}, Users:"] = users_str

with open('bfs.json', 'w',encoding='utf-8') as output_file:
    json.dump(results, output_file, indent=4)


#print_interests(group_users_by_interest(users_tweets))


"""
  
'''
for key in sorted(user_table.keys()):
    users_graph.addVertex(user_table[key])
'''
'''
for i in range(len(users)):
    for j in range(len(users)):
        if i == j:
            continue
        if users[i].person.followers_count == users[j].person.followers_count:
            users_graph.addEdge(user_table[users[i].person.username], user_table[users[j].person.username])
        if users[i].person.following_count == users[j].person.following_count:
            users_graph.addEdge(user_table[users[i].person.username], user_table[users[j].person.username])         #print(users[i].person.following_count)
'''
""" 