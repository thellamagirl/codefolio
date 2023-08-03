# Customer Churn Prediction in the Telecom Industry: Utilizing kNN Classification for Improved Retention Strategies

## Description

This project aims to predict customer churn for a telecom company based on various customer characteristics and purchasing habits. By identifying customers who are likely to churn, the telecom company can take proactive measures to mitigate churn and retain valuable customers. The project utilizes the k-Nearest Neighbors (kNN) classification algorithm to make predictions.

## Features

This project offers the following key features:

1. Data preprocessing: Cleaning the dataset, handling missing values, encoding categorical variables, and scaling numerical features.
2. Exploratory data analysis: Analyzing the relationships between variables and understanding their impact on churn.
3. Model development: Building a kNN classifier and tuning the hyperparameters to optimize performance.
4. Model evaluation: Assessing the model's performance using accuracy, precision, recall, F1-score, and the Area Under the Curve (AUC) of the Receiver Operating Characteristic (ROC) curve.
5. Interpretation: Analyzing the most influential variables in predicting churn and drawing insights for business decision-making.

## Installation & Setup

This project was created using Jupyter Notebook. Jupyter Notebook provides a flexible and interactive environment for coding, data analysis, documentation, and collaboration. Its versatility and ease of use make it popular among researchers, data scientists, educators, and anyone who wants to work with code and data in an interactive and reproducible manner.

For more information on installing the Anaconda Distribution and using Jupyter Notebook, visit https://www.anaconda.com/download

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/thellamagirl/codefolio/tree/main/k-NNClassification
   ``` 

2. Navigate to the project directory:

   ```bash
   cd k-NNClassificationChurnData
   ```

3. Create and activate a virtual environment to isolate project dependencies:

   ```bash
   python3 -m venv myenv    # Create a virtual environment. Replace "myenv" with preferred name of your environment.
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

2. Open the k-NNClassificationofCustomerChurnData.ipynb notebook in Jupyter Notebook.

3. Run the notebook cells to execute the k-NN classification and explore the telecom data.

4. Follow the instructions and comments within the notebook to understand and interpret the analysis results.

## Configuration

This project does not require any additional configuration files or settings, however, if you wish to run the project in Jupyter Notebook it will need to be installed in advance. Visit https://www.anaconda.com/download to begin.

## Contributing

### Bug Reports and Feature Requests
If you encounter a bug or have a feature request, please check the existing issues on the project's GitHub repository to see if it has already been reported. If not, you can open a new issue with a clear and descriptive title, along with a detailed explanation of the problem or feature you'd like to see. Provide any relevant information, such as error messages or examples, that can help in understanding and reproducing the issue.

## Data Source
The data used in this project was provided as part of a course taken at Western Governors University. No reference for the original data source was ever provided. It is unclear if the data was simulated or not. It is telecom data consisting of 10,000 samples and 50 variables. The variables include basic demographic information such as age, number of children, income, and location as well as customer service subscription based information like monthly charges and services they have subscribed to.
 
## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Acknowledgments

I would like to express my sincere gratitude to the following individuals and organizations who have contributed to the completion of this project:

- The many mentors I had during my Master of Data Analytics program for their insightful feedback, suggestions, and assistance.
- My fellow classmates and peers: for engaging in discussions, sharing ideas, and providing constructive feedback.
- The developers and contributors of the open-source libraries and tools used in this project.
- The Stack Overflow and online communities: for their prompt and helpful responses to my questions and challenges.
- My friends and family: for their continuous support, encouragement, and understanding during my studies and the completion of this project.

I am grateful to all those who have directly or indirectly contributed to this project and helped make it a success.

## Contact

You can contact me at thellamagirl@outlook.com

