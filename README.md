# 🍿 AI Movie Recommendation System

## Overview

The AI Movie Recommendation System is a Machine Learning-based web application that recommends movies similar to a selected movie using Content-Based Filtering. The system analyzes movie genres and suggests the most relevant movies based on similarity scores.

Built using Python, Scikit-Learn, and Streamlit, this project demonstrates the practical application of Machine Learning in recommendation systems.

---

## Features

* 🎬 Movie Recommendation Engine
* 🤖 Content-Based Filtering
* 📊 Cosine Similarity Algorithm
* 🎯 Top 5 Similar Movie Recommendations
* 🖥 Interactive Streamlit Dashboard
* ⚡ Fast and Real-Time Recommendations
* 🎈 User-Friendly Interface

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## Project Structure

Movie-Recommender/

├── movies.csv

├── ratings.csv

├── train.py

├── app.py

├── movies.pkl

├── similarity.pkl

├── requirements.txt

└── README.md

---

## How It Works

1. Load movie data from the MovieLens dataset.
2. Extract genre information from each movie.
3. Convert genres into numerical vectors using CountVectorizer.
4. Calculate similarity scores using Cosine Similarity.
5. Recommend the top 5 most similar movies based on the selected movie.

---

## Machine Learning Techniques

### CountVectorizer

Converts movie genre information into numerical feature vectors.

### Cosine Similarity

Measures the similarity between movies and generates recommendations based on the closest matches.

---

## Installation

### Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit
```

### Train the Model

```bash
python train.py
```

This generates:

* movies.pkl
* similarity.pkl

### Run the Application

```bash
streamlit run app.py
```

---

## Applications

* Movie Recommendation Platforms
* OTT Streaming Services
* Entertainment Applications
* Personalized Content Discovery
* Recommendation System Research

---

## Future Enhancements

* Movie Poster Integration
* TMDB API Support
* User Rating-Based Recommendations
* Collaborative Filtering
* Hybrid Recommendation System
* Netflix-Style Interface

---

## Developer

**Adhiban Chakkaravarthy**
B.Tech Artificial Intelligence & Data Science
Peri Institute of Technology

---

## Project Highlights

* Developed a Machine Learning-based recommendation engine.
* Implemented CountVectorizer and Cosine Similarity algorithms.
* Built an interactive Streamlit web application.
* Generated personalized movie recommendations in real time.
* Demonstrated practical applications of Machine Learning in entertainment systems.
