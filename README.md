## FE-595-Final: Machine Learning Trading Strategy
### Contents of the project
1. we have the interactive illustration flask app running at:
[http://18.217.125.148:8000](http://18.217.125.148:8000) and the repository for
the flask app is at [https://github.com/Acatsama0871/FE-595-Final-Web](https://github.com/Acatsama0871/FE-595-Final-Web).

2. For the report of describing the feature engineering, 
model training methodology, result and trading strategy, please refers to the
[file](https://drive.google.com/file/d/1OJvW1QmYbK9ySPwLtOZA_25i6XtdfkSd/view?usp=sharing).

### Repository structure diagram
```
.
├── Data
│   ├── features.csv -> Processed features for ML models
│   └── raw_text -> Raw textural data scrape from twitters
├── Models_train
│   ├── Model_train_P1.ipynb -> Train LDA, QDA, Gaussian Naive Bayes, Logistic Regression, SVM, Random Forest
│   ├── Model_train_P2.ipynb -> Boostring Tree, LSTM, ANN
│   ├── confusion_matrix -> Result confusion matrix of models
│   ├── models -> Saved models
│   ├── tune_ANN -> Log files for tuning ANN
│   └── tune_LSTM -> Log files for tuning LSTM
├── README.md
├── feature_engineering.py -> Process market data and textural data
├── functions
│   ├── __int__.py
│   ├── data_functions -> Functions to download market data, textural data
│   └── model_functions -> Utility function for traning models
└── twitter_downloads.py -> Download Twitter textural data
```
### Purpose
In this project, we are going to use the machine learning method to predict 
the weekly SPY’s price movement direction. Based on the prediction of price
movement direction, we implemented a trading strategy. Please see the [file](https://drive.google.com/file/d/1OJvW1QmYbK9ySPwLtOZA_25i6XtdfkSd/view?usp=sharing)
for detail of our methodology of training the model, model selection result and
trading strategy.

The basic steps are as follows:
1. Scrape the data from Twitter and use NLP to generate the sentiment scores. 
2. Download the OHLC market data and derive the features.
3. Combine the sentiment scores of tweets data and features from market data
to obtain total features.
4. Fit and find best parameters for the LDA, QDA, Gaussian naive Bayes model, logistic regression, random forest
boosting tree, support vector machine, LSTM, ANN models.
5. Select the best model according to cross-validation accuracy.
6. Implement trading strategy based on the best model.

To backtest our trading strategy, we also implemented a [flask app](https://github.com/Acatsama0871/FE-595-Final-Web). The user of
the app are able to choose a time period between 2020-01-06 and 2020-12-07 to 
backtest strategy.

### Inspiration
In this project, we want to investigate whether we can use ML model to predict
the price movement direction of a stock. We download the market data and calculate
some technical indicators. We think the technical indicators may be a good
predictor to detect the potential price movement direction. Besides, we think
the attitude of investor might also play a import role in determining the
price movement direction. To measure the attitude of the investors, we scrape
the tweets and calculated the sentiment score. Combining these features, 
we fit the different models to see our prediction accuracy.

### Deployment
We have an interactive flask app to backtest the ML trading strategy within
2020-01-06 to 2020-12-07. For the detail of deployment the flask app, please
see 
[https://github.com/Acatsama0871/FE-595-Final-Web](https://github.com/Acatsama0871/FE-595-Final-Web).

### Usage of project
To generate the reproducible results as we described in the [file](https://drive.google.com/file/d/1OJvW1QmYbK9ySPwLtOZA_25i6XtdfkSd/view?usp=sharing). Please
download the repository and run code in following way:
```
1. twitter_downloads.py
2. feature_engineering.py
3. Model_train_P1.ipynb
4. Model_train_P2.ipynb
```

### Contributors
* Haohang Li
* Baihaog Huang
* Mengyuan He
* Haonan Wang
* Zichen Gao
