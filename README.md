
# Movie Recommender System

Welcome to the Movie Recommender System project! This project uses the TMDB 5000 Movies Dataset to build a recommendation system that suggests movies based on user input. The model is built using various Python libraries and is deployed as a web application using Streamlit.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Libraries Used](#libraries-used)
- [Model Details](#model-details)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project aims to provide movie recommendations based on content similarity. The model processes the TMDB 5000 Movies Dataset and uses natural language processing and machine learning techniques to suggest movies similar to a user-selected movie.

## Dataset
The data used for this project is the TMDB 5000 Movies Dataset available on Kaggle. The dataset includes movie metadata, such as genres, keywords, cast, crew, etc.

- [TMDB 5000 Movies Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/code)

## Libraries Used
The following libraries are used in this project:

- [Scikit-learn](https://scikit-learn.org/stable/): For CountVectorizer, TfidfVectorizer(current) and cosine similarity calculations.
- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [Numpy](https://numpy.org/): For numerical operations.
- [NLTK](https://www.nltk.org/): For natural language processing (PorterStemmer).
- [Pickle](https://docs.python.org/3/library/pickle.html): For serializing and saving the model.
- [Streamlit](https://streamlit.io/): For building and deploying the web application.

## Model Details
The recommendation model is based on content similarity. Here are the key steps involved:

1. **Data Preprocessing**: Cleaning and preparing the dataset.
2. **Feature Extraction**: Using CountVectorizer/TfidfVectorizer to convert text data into feature vectors.
3. **Similarity Calculation**: Calculating cosine similarity between movies.
4. **Recommendation**: Suggesting movies based on similarity scores.
5. **Model Serialization**: Using Pickle to save the trained model for future use.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movies-recommender-system.git
   cd movies-recommender-system
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset from Kaggle and place it in the appropriate directory.

## Usage
To run the Streamlit app locally, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the web application in your browser.

## Screenshots
![image](https://github.com/user-attachments/assets/f827129c-4684-4209-8c9a-bada6923a184)

![image](https://github.com/user-attachments/assets/6957ea5b-0c4e-4a87-ade9-3692a3d03625)


## Deployment
The web application is deployed using Streamlit. You can access the live application here:

- [Movie Recommender System](https://movie-recommender-buddy.streamlit.app/)

To deploy your version, follow these steps:

1. Push your code to a GitHub repository.
2. Connect your repository to Streamlit Cloud and deploy the app.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
