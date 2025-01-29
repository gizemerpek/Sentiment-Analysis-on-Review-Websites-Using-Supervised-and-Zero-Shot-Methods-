# Sentiment-Analysis-on-Review-Websites-Using-Supervised-and-Zero-Shot-Methods-
In this project, I scraped review data from the Trustpilot website. 
I then performed sentiment analysis using a supervised network. 
I built the model on labeled data and then applied zero-shot sensitivity analysis technique to the same data 
for comparison.
I use web scraping tools BeautifulSoup. I collect relevant fields such as review text, rating, date, and user information.
Data Cleaning and Preprocessing:
First, I standardized the text data by converting all text to lowercase, removing special characters, and cleaning unnecessary spaces. Then, I applied NLP preprocessing techniques, including tokenization, stop-word removal, and lemmatization.

Supervised Sentiment Analysis:

Data Labeling: I manually labeled a subset of the dataset with sentiment categories: Positive, Neutral, and Negative.
Model Training: I trained different machine learning models for supervised sentiment analysis, including Support Vector Machines (SVM), Logistic Regression, Random Forest, and Naïve Bayes.
Evaluation: I evaluated the models on a test dataset using accuracy, precision, recall, and F1-score as performance metrics.

Zero-Shot Sentiment Analysis:

Model Selection: I selected a pre-trained zero-shot model, specifically a BERT-based model, to classify sentiment without task-specific training.
Implementation: Using this model, I directly classified text as Positive, Neutral, or Negative.
Evaluation: I assessed the performance of the zero-shot model using the same test dataset.

Results Comparison and Analysis:
I compared the performance of the supervised and zero-shot models using accuracy, precision, recall, and F1-score. I observed that supervised learning models provided higher accuracy when trained on a specific dataset, while the zero-shot model offered more flexibility.
