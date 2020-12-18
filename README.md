## FE-595-Final: Machine Learning Trading Strategy
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
In this project, we implemented 

### 