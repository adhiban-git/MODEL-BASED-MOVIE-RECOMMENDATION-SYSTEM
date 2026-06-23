import streamlit as st
import pickle

# Page Config
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Load Files
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Sidebar
st.sidebar.title("🎬 Movie Recommender")

st.sidebar.info(
    """
    AI Movie Recommendation System

    Built Using:
    - Python
    - Scikit-Learn
    - Streamlit
    - Cosine Similarity
    """
)

# Main Title
st.title("🍿 AI Movie Recommendation System")

st.write(
    "Get personalized movie recommendations instantly using Machine Learning."
)

# Statistics
st.metric(
    label="Movies Available",
    value=len(movies)
)

# Movie List
movie_list = movies["title"].values

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movie_list
)

# Recommendation Function
def recommend(movie):

    movie_index = movies[
        movies["title"] == movie
    ].index[0]

    distances = similarity[movie_index]

    movie_recommendations = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_recommendations:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations


# Button
if st.button("🎬 Recommend Movies"):

    st.balloons()

    recommendations = recommend(
        selected_movie
    )

    st.subheader(
        f"Movies Similar to '{selected_movie}'"
    )

    for i, movie in enumerate(
        recommendations,
        start=1
    ):
        st.success(
            f"{i}. {movie}"
        )

# Footer
st.markdown("---")

st.caption(
    "Created by Adhiban Chakkaravarthy "
)