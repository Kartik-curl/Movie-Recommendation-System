
import streamlit as st
from model import recommend
import pandas as pd
import pickle
from modules import movie_detail,action_and_adventure


st.markdown("""
<style>
div.stButton > button {
    background-color: rgb(34, 115, 186);  
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: rgb(28, 93, 150);
}
</style>
""", unsafe_allow_html=True)
        

with open('dataset.pkl','rb') as file :
    data = pickle.load(file)   

        
st.set_page_config(page_title='movie recommedation system',layout='wide')
st.title("Movie Recommendation System")

data['title'] = data['title'].apply(lambda x: str(x).capitalize())

movie_name = st.selectbox('Please Select a Movie',options=data['title'])

if st.button("Recommend"):
        movies,id= recommend(movie_name)
        try:
            dataframe = pd.read_pickle('poster.pkl')
            poster_list = []
            for i in id:
                if i in dataframe['id']:
                    poster_list.append(dataframe.loc[dataframe['id']==i,'poster'].iloc[0])
                else:
                    result = movie_detail(i)
                    poster_list.append(result[0])
            
    
            st.info("Best Movies Recommended for you: ")
            col1,col2,col3,col4,col5 =st.columns(5)
            with col1:
                st.image(poster_list[0])
                st.subheader(movies[0].capitalize())
            with col2:
                st.image(poster_list[1])
                st.subheader(movies[1].capitalize())
            with col3:
                st.image(poster_list[2])
                st.subheader(movies[2].capitalize())
            with col4:
                st.image(poster_list[3])
                st.subheader(movies[3].capitalize())
            with col5:
                st.image(poster_list[4])
                st.subheader(movies[4].capitalize())
        
        except:
            st.text("Best Movies Recommended for you: ")
            st.subheader(f"1. {movies[0].capitalize()}")
            st.subheader(f"2. {movies[1].capitalize()}")
            st.subheader(f"3. {movies[2].capitalize()}")
            st.subheader(f"4. {movies[3].capitalize()}")
            st.subheader(f"5. {movies[4].capitalize()}")

col1,col2 = st.columns(2)
action,adventure = action_and_adventure()
with col1:
    st.subheader('10 Action Movies to watch:')
    for i in range(10):
        st.text(f"{i+1}. {action[i]}")
with col2:
    st.subheader('10 Adventure movies to watch:')
    for i in range(10):
      st.text(f"{i+1}. {adventure[i]}")
st.subheader("The Movies You Can Watch:")
col1,col2,col3,col4,col5 = st.columns(5)
df = pd.read_pickle('poster.pkl')
data = pd.read_pickle('dataset.pkl')
for i in range(0,500,5):
     with col1:
        st.image(df.iloc[i].poster)
        st.text((data.loc[data['id']==df.iloc[i].id,'title'].iloc[0]).capitalize())
     with col2:
        st.image(df.iloc[i+1].poster)
        st.text((data.loc[data['id']==df.iloc[i+1].id,'title'].iloc[0]).capitalize())
     with col3:
        st.image(df.iloc[i+2].poster)
        st.text((data.loc[data['id']==df.iloc[i+2].id,'title'].iloc[0]).capitalize())
     with col4:
        st.image(df.iloc[i+3].poster)
        st.text((data.loc[data['id']==df.iloc[i+3].id,'title'].iloc[0]).capitalize())
     with col5:
        st.image(df.iloc[i+4].poster)
        st.text((data.loc[data['id']==df.iloc[i+4].id,'title'].iloc[0]).capitalize())