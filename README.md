# 🎬 Movie Recommendation System

This is a content-based **Movie Recommendation System** built using **Python**, **Streamlit**, and **scikit-learn**. It allows users to enter a movie title and receive top 5 movie suggestions based on tag relevance and similarity.

---

## 📂 Dataset

This project uses the **MovieLens 20M Dataset** by GroupLens, which contains 20 million ratings and tag applications applied to 27,000 movies by 138,000 users.

📦 [Click here to view/download the dataset on Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)

**Files used:**
- `movies.csv`
- `genome_scores.csv`
- `genome_tags.csv`

---

## 🚀 Project Highlights

- 🔍 **Search by title**: Suggests movies similar to your input using part of the name.
- 🧠 **Content-based filtering**: Uses movie genome tags and cosine similarity.
- 📊 **Data scaling**: Features are normalized using `MinMaxScaler`.
- ⚙️ **Fast performance**: Efficient pre-processing for near-instant recommendations.
- 🖥️ **Interactive UI**: Built with Streamlit for a smooth, user-friendly experience.

---

## 🛠️ Tools & Technologies

- `Python`
- `Pandas`
- `Scikit-learn`
- `Streamlit`
- `Cosine Similarity`
- `MinMaxScaler`

---

## 👨‍💼 Why this Project?

This project showcases my practical knowledge of:

- Building ML-based recommender systems.
- Real-world data preprocessing and similarity calculations.
- Designing interactive, deployable web apps with **Streamlit**.
- Creating clean, recruiter-friendly solutions with user experience in mind.

---

## 💡 How it Works

1. **Load Data**: Movie titles, genome tags, and scores.
2. **Preprocess**: Pivot the tag relevance matrix and normalize.
3. **Similarity Matrix**: Compute cosine similarity between all movies.
4. **Recommend**: Based on user input, find the closest match and suggest similar movies.

---

## 🖥️ Run it Locally

```bash
python -m streamlit run app.py
