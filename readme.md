# Spotify Valence Explorer 🎵

**Spotify Valence Explorer** visualizes how **valence** (Spotify’s measure of musical positivity) interacts with other audio features across **232,725 tracks** and **26 genres**.  
This project was created as part of the Information Visualization final project.

---

## 🚀 Features
- **Interactive Dashboard**: Built with Dash/Streamlit for real-time exploration.  
- **Multivariate Filtering**: Filter tracks by features like tempo, energy, danceability, and valence.  
- **Genre Comparison**: Compare distributions and relationships of features across genres.  
- **Dimensionality Reduction**: PCA and UMAP embeddings to explore song clusters.  
- **Linked Visualizations**: Scatterplots, parallel coordinates, and correlation analysis.  

---

## 🧑‍🤝‍🧑 Team
- **Saanavi Goyal**  
- **Nirath Hussan**  
- **Ezzeldin Moussa**  

---

##  Running the Program

```
cd dashboard 
python app.py
```

📊 Dataset

- Source: Ultimate Spotify Tracks DB (Kaggle) + Spotify API
- Tracks: 232,725
- Genres: 26
- Preprocessing: Data cleaned and normalized for visualization

📌 Notes

The dashboard supports interactive filtering, cross-feature exploration, and genre-level analysis. For dimensionality reduction (PCA/UMAP), ensure scikit-learn and umap-learn are installed
