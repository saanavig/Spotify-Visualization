# **Project Proposal – Spotify Valence Explorer**
**Course:** Information Visualization  
**Team:** Saanavi Goyal, Nirath Hussan, Ezzeldin Moussa
**Repository:** https://github.com/yourusername/Spotify-Visualization  
**Dataset:** Ultimate Spotify Tracks DB (Kaggle) + Custom Genre Subsets (~232k tracks)

---

## **1. Abstract**

This project aims to explore how **valence**—Spotify’s measure of musical positivity or emotional brightness—interacts with the full set of Spotify’s audio features across more than 230,000 songs from 26 distinct genres. While many existing music dashboards visualize simple statistics such as popularity, genre counts, or the top tracks of certain artists, few attempt to analyze emotional tone as a multivariate phenomenon embedded within a high-dimensional audio feature space. Valence is uniquely interesting because it attempts to quantify the *emotional character* of a track, yet the ways in which it relates to features such as danceability, energy, tempo, acousticness, and speechiness is not straightforward.

Using a large, real Spotify dataset enriched with 10,000 samples per genre, this project will construct an **interactive visual analytics dashboard** that allows users to: (1) explore valence distributions within and across genres, (2) identify multivariate relationships between valence and other audio characteristics, (3) visualize clusters and embeddings of songs, and (4) perform genre-level comparisons through dynamic filtering, brushing, and details-on-demand. The final system will support discovery of patterns that are not visible through simple scatterplots, and provide a richer understanding of how “emotional tone” emerges across contemporary music.

---

## **2. Problem and Motivation**

Spotify provides several high-level audio features for each track, but the interplay between these features—especially **valence**—is under-explored. Understanding how emotional brightness relates to tempo, energy, and genre can provide insights for:

- Music recommendation systems
- Playlist curation
- Genre evolution analysis
- Artist stylistic profiling
- Emotional contour mapping of music libraries

The visual analytics approach is well-suited to this problem because valence does not depend on a single feature. It emerges from **complex, multivariate relationships** that require both aggregate and interactive exploration. This problem is therefore ideal for applying visualization principles learned in class, including overview-first design, multivariate analysis, high-dimensional reduction, and interactive filtering.

---

## **3. Background and Dataset Description**

Previous Spotify visualizations (such as Spotify Wrapped clones, basic popularity charts, or simple genre distributions) primarily rely on 1–2 variables. Visualizations that do incorporate valence often present only a scatterplot or a single regression line, limiting analytical depth.

### **Source**
- Kaggle: *Ultimate Spotify Tracks DB*  
  https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db  
- Supplemented with custom Spotify API pulls (approx. 10,000 tracks per genre).  
- Total: **232,725 tracks** across **26 genres**.

### **Attributes (20+)**
- Numerical audio features:  
  `valence`, `energy`, `danceability`, `instrumentalness`, `acousticness`, `liveness`,  
  `speechiness`, `loudness`, `tempo`, `duration_ms`
- Categorical features:  
  `genre`, `key`, `mode`, `time_signature`
- Additional metadata:  
  `track_name`, `artist`, release year (if available), popularity (if present)

### **Why this dataset fits the course criteria**
- **Large (≫ 5,000 records)** → 232k tracks  
- **Multivariate** → more than 15 meaningful attributes  
- **Real-world** → backed by Spotify’s API  
- **Complex enough** to require filtering, aggregation, DR, and interactive visual tools  
- **Genre diversity** enables comparative analysis and storytelling

---

## **5. Visualization Goals and Tasks**

### **Task 1 — Overview of Emotional Tone**
- Show global distribution of valence across all tracks  
- Genre-level summaries (box plots, treemaps, ridge plots)

### **Task 2 — Multivariate Relationships**
- Explore correlations between valence and:  
  - danceability  
  - energy  
  - acousticness  
  - loudness  
  - tempo  
  - instrumentalness  
- Use scatter matrices and parallel coordinate plots

### **Task 3 — High-Dimensional Structure**
- Apply PCA, UMAP, or t-SNE to embed all songs into 2D  
- Color points by valence or genre  
- Allow users to filter by feature or valence range  
- Identify “clusters of emotion” in the feature space

### **Task 4 — Genre-Level Deep Dives**
- Compare how valence behaves differently in:  
  rock vs pop vs EDM vs hip-hop vs jazz vs classical  
- Genre switching via dropdown  
- Genre-specific feature correlation panels

### **Task 5 — Details-on-Demand**
- Hover or click on points for:
  - track name
  - artist
  - exact feature values
  - genre metadata

---

## **6. Proposed Dashboard Design**

The final system will be built as a **multi-view interactive dashboard**. Planned components:

### **1. Overview Panel**
- Valence distribution histograms
- Genre-level comparison

### **2. Feature Relationship Panel**
- Scatterplot matrix (SPLOM) or linked scatterplots
- Parallel coordinates for high-dimensional filtering

### **3. Embedding Panel**
- 2D projection of all songs (PCA / UMAP)
- Color-coded by valence, genre, or popularity
- Brushing to highlight corresponding genre samples

### **4. Filter Sidebar**
- Genre dropdown
- Range sliders for valence, tempo, energy, etc
- Search bar for artist or track

### **5. Details Panel**
- Expanded track info
- Audio feature summary
- Optional: artist/genre biography snippet

---

## **7. Technical Approach**

### **Tools / Libraries**
- Python (Pandas, NumPy, Scikit-learn) for cleaning + DR
- Plotly / Dash OR D3.js for interactive components
- Altair for prototype visuals
- GitHub for version control

### **Data Preprocessing**
- Remove duplicates
- Handle missing values
- Standardize audio features
- Reduce sampling density for computational efficiency
- Generate intermediate summary datasets
- Compute correlations and PCA embeddings

### **Interactivity**
- Brushing & linking across scatterplots
- Genre filtering
- Dynamic axis selection
- Hover tooltips
- Live updating embeddings (optional)
