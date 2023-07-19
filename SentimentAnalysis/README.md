# Unveiling Sentiments: Exploring Customer Reviews using Logistic Regression, Random Forest, and CNN-LSTM

## Overview

This project focuses on sentiment analysis, which involves the classification of text data into different sentiment categories such as positive or negative. The goal is to build and compare multiple models to accurately classify customer reviews from various sources based on their sentiment.

## Features

### Three different models are implemented and compared:

Logistic Regression: This model uses a logistic regression algorithm to perform sentiment analysis on the customer reviews. It is a classic machine learning approach widely used for binary classification tasks.

Random Forest: The random forest model, a popular ensemble learning technique, is employed for sentiment analysis. It combines multiple decision trees to make predictions and provides robustness against overfitting.

CNN-LSTM Neural Network: A deep learning model consisting of convolutional neural network (CNN) and long short-term memory (LSTM) layers is utilized for sentiment analysis. This model has the ability to capture both local and global dependencies within the text data.

## Installation and Setup

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/thellamagirl/codefolio/tree/main/SentimentAnalysis
   ``` 

2. Navigate to the project directory:

   ```bash
   cd SentimentAnalysis
   ```

3. Create and activate a virtual environment to isolate project dependencies:

   ```bash
   python3 -m venv myenv    # Create a virtual environment
   source myenv/bin/activate    # Activate the virtual environment
   ```

   This step is optional but recommended to keep your project dependencies separate from other Python installations on your system.

4. Install the required libraries and dependencies using `pip` and the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the necessary packages and their specified versions.

## Usage

1. Launch Jupyter Notebook:

   ```bash
    jupyter notebook
   ```
2. Open the SentimentAnalysisExploration.ipynb notebook in Jupyter Notebook.

3. Run the notebook cells to execute the three models and explore the review data.

4. Follow the instructions and comments within the notebook to understand and interpret the analysis results.

## Configuration

This project utilizes pre-trained word embeddings from the FastText corpora. This will need to be downloaded prior to running the notebook. You can find it here: https://fasttext.cc/

If you wish to run the project in Jupyter Notebook it will need to be installed in advance. Visit https://www.anaconda.com/download to begin.

## Contributing

### Bug Reports and Feature Requests
If you encounter a bug or have a feature request, please check the existing issues on the project's GitHub repository to see if it has already been reported. If not, you can open a new issue with a clear and descriptive title, along with a detailed explanation of the problem or feature you'd like to see. Provide any relevant information, such as error messages or examples, that can help in understanding and reproducing the issue.

## Data Source

The data used in this project was provided as part of a course taken at Western Governors University. The reference for the dataset is:

Kotzias, D., Denil, M., De Freitas, N., & Smyth, P. (2015). From Group to Individual Labels using Deep Features. In Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

### From the readme.txt from the data file:

### Dataset Details:
Score is either 1 (for positive) or 0 (for negative)	
The sentences come from three different websites/fields:

imdb.com
amazon.com
yelp.com

For each website, there exist 500 positive and 500 negative sentences. Those were selected randomly for larger datasets of reviews. 

We attempted to select sentences that have a clearly positive or negative connotation, the goal was for no neutral sentences to be selected.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Acknowledgments

I would like to express my sincere gratitude to the following individuals and organizations who have contributed to the completion of this project:

- The many mentors I had during my Master of Data Analytics program for their insightful feedback, suggestions, and assistance.
- My fellow classmates and peers: for engaging in discussions, sharing ideas, and providing constructive feedback.
- The developers and contributors of the open-source libraries and tools used in this project.
- The Stack Overflow and online communities: for their prompt and helpful responses to my questions and challenges.
- My friends and family: for their continuous support, encouragement, and understanding during my studies and the completion of this project.
- I am grateful to all those who have directly or indirectly contributed to this project and helped make it a success.

## Contact

You can contact me at thellamagirl@outlook.com

