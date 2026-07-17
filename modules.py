import pickle
import random
import requests
import pandas as pd
sessions = requests.Session()

def movie_detail(movie_id):
        headers = { "Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMTI0MWM3NzE3NmRiMTgwNTFlZDdkZTQ1ZmYyMjljYiIsIm5iZiI6MTc4NDE3NzUwMC45MTUsInN1YiI6IjZhNTg2MzVjM2UwYTUzOTBiYTJmZmJkZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dHVz7HOut_CbyEO1P1xgaKKpAvAZwzXUXI4bq9kdZvc",
            
            "accept":"application/json"}
        
        df =pd.read_pickle('poster.pkl')
        
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        data = sessions.get(url,headers = headers,)
        poster_path = data.json()["poster_path"]
        homepage= data.json()['homepage']
        poster = f"https://image.tmdb.org/t/p/w200/{poster_path}"
        new_record = {
            'id':movie_id,
            'poster':poster,
            'homepage':homepage

        }
        df.loc[len(df)] = new_record
        df.to_pickle('poster.pkl')
        return (poster,homepage)

def action_and_adventure():
    with open('dataset.pkl','rb') as file:
        df= pickle.load(file)
    action =adventure = []

    for i in range(1,len(df['id'])):
        if 'action' in df.iloc[i].tags:
            action.append(df.iloc[i].title)
        elif 'adventure' in df.iloc[i].tags:
            adventure.append(df.iloc[i].title)
        
    ten_action =[]
    ten_adventure =[]
    c1=c2= 0
    while c1<10:
        idx = random.randrange(0,len(action)-1)
        if action[idx] not in ten_action :
            ten_action.append(action[idx].capitalize())
            c1+=1
    while c2<10:
        idx = random.randrange(0,len(adventure)-1)
        if adventure[idx] not in ten_adventure :
            ten_adventure.append(adventure[idx].capitalize())
            c2+=1       
    return ten_action,ten_adventure