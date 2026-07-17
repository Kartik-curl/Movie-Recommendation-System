import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle 
import requests
sessions = requests.Session()
from sklearn.feature_extraction.text import TfidfVectorizer
ps = PorterStemmer()
tfid = TfidfVectorizer(max_features= 5000,stop_words='english')

data1 = pd.read_csv('datasets/tmdb_5000_movies.csv')
data2 = pd.read_csv('datasets/tmdb_5000_credits.csv')
movies = pd.DataFrame(data1)
credits = pd.DataFrame(data2)
#print(movies.shape)
#print(credits.shape)
df =movies.merge(credits,on='title')
df = df[['id','genres','keywords','overview','title','cast','crew']]
#print(df.notna().sum())
df = df.dropna()

def convert(obj):
    genre = []
    for i in ast.literal_eval(obj):
        genre.append(i['name'])
    return genre

def cast_convert(obj): 
    casts = []
    for i in ast.literal_eval(obj):
        casts.append(i['name'])
    return casts[:5]

def get_director(obj):
    director=[]
    for i in ast.literal_eval(obj):
        if i['job'] == "Director":
            director.append(i['name'])
    return director

#preprocess each column
df['genres'] = df['genres'].apply(convert)
df['keywords'] = df['keywords'].apply(convert)
df['cast'] = df['cast'].apply(cast_convert)
df['crew'] =df['crew'].apply(get_director)

#to remove whitespaces so that model understand whole word
df['genres'] = df['genres'].apply(lambda x:[i.replace(" ","") for i in x])
df['cast'] = df['cast'].apply(lambda x:[i.replace(" ","") for i in x])
df['crew']=df['crew'].apply(lambda x:[i.replace(" ","") for i in x])
df['keywords'] = df['keywords'].apply(lambda x:[i.replace(" ","") for i in x])

#convert overview words to list
df['overview'] = df['overview'].apply(lambda x: str(x).split())

#print(df['genres'][0])
#print(df['keywords'][0])
#print(df['cast'][0])
#print(df['crew'][0])
#print(df['overview'][0])


#new column tags contans all keywords
df['tags'] = df['genres']+df['keywords']+df['cast']+df['overview']+df['crew']

#new dataframe with requied column tag
new_df= df[['id','title','tags']]

#convert tags datatype to string from list
new_df['tags'] =new_df['tags'].apply(lambda x:' '.join(x))

#lowercase the data
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
new_df['title'] = new_df['title'].apply(lambda x:x.lower())

#stemming of words
def stem(obj):
    y= []
    for i in obj.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

#vectorization of data
vector = tfid.fit_transform(new_df['tags']).toarray()


#similarity of all with each other 
similarity = cosine_similarity(vector)
with open("dataset.pkl",'wb') as file:
    pickle.dump(new_df,file)
    
def recommend(movie):
    movie = movie.lower()
    idx = new_df[new_df['title'] == movie].index[0]
    distance = list(enumerate(similarity[idx]))
    distance = sorted(distance,reverse=True,key = lambda x: x[1])[1:6]
    movies = []
    id=[]
    for i in distance:
        movies.append(new_df.iloc[i[0]].title)
        id.append(new_df.iloc[i[0]].id)
    return movies,id



