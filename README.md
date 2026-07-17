# 🎬 Movie Recommender System

A content-based Movie Recommender System built with **Streamlit**, **Scikit-learn**, and the **TMDB API**. The application recommends movies based on their genres using **TF-IDF Vectorization** and **Cosine Similarity**, and displays high-quality movie posters.

---
##Live Link - https://movie-recommendation-system-by-kartik.streamlit.app/
## 🚀 Features

- 🔍 Search movies by title
- 🎯 Get top 10 similar movie recommendations
- 🎭 Genre-based recommendation using TF-IDF Vectorizer
- 📊 Cosine Similarity for finding similar movies
- 🖼️ Display movie posters using TMDB API
- ⚡ Fast and interactive Streamlit interface
- 🎬 Suggests 10 Action and 10 Adventure movies
- 📱 Clean and responsive UI

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- TMDB API

---

## 📚 Machine Learning Concepts Used

### TF-IDF Vectorizer

The **TF-IDF (Term Frequency-Inverse Document Frequency)** Vectorizer converts movie genres into numerical feature vectors.

- Treats each movie's genres as a text document.
- Gives higher importance to unique genres.
- Converts text into sparse numerical vectors.

Example:

```
Action Adventure Fantasy
```

↓

```
[0.65, 0.48, 0.59, ...]
```

---

### Cosine Similarity

Cosine Similarity measures how similar two movie vectors are.

Formula:

```
Cosine Similarity = (A · B) / (||A|| × ||B||)
```

- Value ranges from **0 to 1**
- **1** → Exactly similar
- **0** → Completely different

The application computes similarity between every pair of movies and recommends the most similar ones.

---

## 📂 Project Structure

```
Movie-Recommender-System/
│ 
├── app.py                  # Streamlit application
|── model.py                 # model
|── modules.py                 #other functions
├── dataset.pkl             
├── poster.pkl          
├── requirements.txt
├── README.md
└── datasets
    |──tmdb_5000_credits.csv
    |──tmdb_5000_movies.csv
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Kartik-curl/Movie-Recommendation-System.git
```

### Move into the project directory

```bash
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Load the movie dataset.
2. Combine movie genres into a single text feature.
3. Convert genres into TF-IDF vectors.
4. Compute Cosine Similarity between all movies.
5. User selects a movie.
6. Retrieve the similarity scores.
7. Recommend the top 5 most similar movies.
8. Fetch movie posters using the TMDB API.
9. Display recommendations along with posters.
10. Show curated lists of 10 Action and 10 Adventure movies.

---



## 📦 Dataset

The project uses a movie dataset containing:

- Movie ID
- Movie Title
- Overview
- Cast 
- Crew
- Timestamps
- Duration
- Original Title
- Genres
- Ratings

---

## 🔗 TMDB API

Movie posters are fetched dynamically using the **TMDB API**.

Poster URL format:

```
https://image.tmdb.org/t/p/w200/<poster_path>
```

---

## 📈 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- User Authentication
- Movie Ratings
- Watchlist Feature
- Trailer Integration
- Genre Filters
- Search Suggestions
- Dark Mode
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

**Kartik Thakur**

- AI & Machine Learning Enthusiast
- Python Developer
- Streamlit Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it with others!
