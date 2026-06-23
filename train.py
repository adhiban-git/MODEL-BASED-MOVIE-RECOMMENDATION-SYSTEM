import pandas as pd
import pickle
import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 60)
print("🎬 AI MOVIE RECOMMENDATION SYSTEM")
print("🚀 Training Started...")
print("=" * 60)

start_time = time.time()

# Load Dataset
print("\n📂 Loading movies.csv...")
movies = pd.read_csv("movies.csv")

print(f"✅ Dataset Loaded Successfully")
print(f"📊 Total Movies: {len(movies)}")

# Handle Missing Values
movies["genres"] = movies["genres"].fillna("")

print("\n🔄 Creating Feature Matrix...")

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(
    movies["genres"]
).toarray()

print("✅ Feature Matrix Created")

# Similarity Calculation
print("\n🧠 Calculating Cosine Similarity Matrix...")

similarity = cosine_similarity(vectors)

print("✅ Similarity Matrix Generated")

# Save Files
print("\n💾 Saving Trained Files...")

pickle.dump(
    movies,
    open("movies.pkl", "wb")
)

pickle.dump(
    similarity,
    open("similarity.pkl", "wb")
)

end_time = time.time()

print("\n" + "=" * 60)
print("🎉 TRAINING COMPLETED SUCCESSFULLY")
print("✅ movies.pkl saved")
print("✅ similarity.pkl saved")
print(f"⏱ Time Taken: {end_time - start_time:.2f} seconds")
print("=" * 60)