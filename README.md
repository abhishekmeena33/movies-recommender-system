
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
This project aims to provide movie recommendations based on content similarity. The model processes the TMDB 5000 Movies Dataset and uses natural language processing and machine learning techniques to suggest movies that are similar to a user-selected movie.

## Dataset
The data used for this project is the TMDB 5000 Movies Dataset available on Kaggle. The dataset includes metadata about movies, such as genres, keywords, cast, crew, and more.

- [TMDB 5000 Movies Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/code)

## Libraries Used
The following libraries are used in this project:

- [Scikit-learn](https://scikit-learn.org/stable/): For CountVectorizer and cosine similarity calculations.
- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [Numpy](https://numpy.org/): For numerical operations.
- [NLTK](https://www.nltk.org/): For natural language processing (PorterStemmer).
- [Pickle](https://docs.python.org/3/library/pickle.html): For serializing and saving the model.
- [Streamlit](https://streamlit.io/): For building and deploying the web application.

## Model Details
The recommendation model is based on content similarity. Here are the key steps involved:

1. **Data Preprocessing**: Cleaning and preparing the dataset.
2. **Feature Extraction**: Using CountVectorizer to convert text data into feature vectors.
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
![image](https://github.com/abhishekmeena33/movies-recommender-system/assets/118628637/cae17418-5479-4830-80b0-9be088461c24)
![image](https://github.com/abhishekmeena33/movies-recommender-system/assets/118628637/6a8ee307-9508-48b1-a645-8685c8669c93)


## Deployment
The web application is deployed using Streamlit. You can access the live application here:

- [Movie Recommender System](https://movie-recommender-buddy.streamlit.app/)

To deploy your own version, follow these steps:

1. Push your code to a GitHub repository.
2. Connect your repository to Streamlit Cloud and deploy the app.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify any section as per your requirement. Also, don't forget to replace the placeholder URL with your actual GitHub repository link and add screenshots in the designated section.
