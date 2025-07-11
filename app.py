import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load data
@st.cache_data
def load_data():
    movies = pd.read_csv("movie.csv")
    genome_scores = pd.read_csv("genome_scores.csv")
    genome_tags = pd.read_csv("genome_tags.csv")
    
    genome_data = pd.merge(genome_scores, genome_tags, on='tagId')
    movie_tag_matrix = genome_data.pivot_table(index='movieId', columns='tag', values='relevance', fill_value=0)

    scaler = MinMaxScaler()
    movie_tag_matrix_scaled = scaler.fit_transform(movie_tag_matrix)
    similarity_matrix = cosine_similarity(movie_tag_matrix_scaled)
    
    movie_id_to_title = dict(zip(movies['movieId'], movies['title']))
    title_to_movie_id = {v: k for k, v in movie_id_to_title.items()}
    
    return movies, movie_tag_matrix, similarity_matrix, movie_id_to_title, title_to_movie_id

movies, movie_tag_matrix, similarity_matrix, movie_id_to_title, title_to_movie_id = load_data()

# Find closest match
def find_closest_movie(title_input):
    title_input = title_input.lower()
    matches = [title for title in movies['title'] if title_input in title.lower()]
    return matches[0] if matches else None

# Recommendation logic
def get_recommendations(movie_input, top_n=5):
    matched_title = find_closest_movie(movie_input)
    if not matched_title:
        return f"No match found for '{movie_input}'", []

    movie_id = title_to_movie_id.get(matched_title)
    if movie_id is None or movie_id not in movie_tag_matrix.index:
        return f"Movie '{matched_title}' not found in similarity matrix.", []

    idx = movie_tag_matrix.index.get_loc(movie_id)
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i for i, _ in sim_scores[1:top_n+1]]
    recommended_movie_ids = movie_tag_matrix.index[top_indices]
    recommended_titles = [movie_id_to_title[mid] for mid in recommended_movie_ids]

    return matched_title, recommended_titles

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.markdown("Find movies similar to your favorite! Just enter part of a title below:")

movie_input = st.text_input("Enter a movie title:", placeholder="e.g., Finding Nemo")

if movie_input:
    matched, results = get_recommendations(movie_input)

    if isinstance(results, list) and results:
        st.success(f"Top 5 recommendations similar to **{matched}**:")
        for i, rec in enumerate(results, 1):
            st.write(f"**{i}.** {rec}")
    else:
        st.error(matched)

    