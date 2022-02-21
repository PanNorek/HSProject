# Describe datasets

Readme will be updated soon.

# English Datasets

## Dataset 1
The dataset comes from kaggle (link here: https://www.kaggle.com/kazanova/sentiment140)
It contains the following 6 fields:
1. target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
2. ids: The id of the tweet ( 2087)
3. date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
4. flag: The query (lyx). If there is no query, then this value is NO_QUERY.
5. user: the user that tweeted (robotickilldozr)
6. text: the text of the tweet (Lyx is cool)

## Dataset 2 
hateval2019: it includes English tweets about hate speech against women and immigrants
1. a numeric ID that uniquely identifies the tweet within the dataset (id column)
2. the text of the tweet (text column)
3. a binary value {1|0} indicating if hate speech is occurring against one of the given targets, women or immigrants (HS column)
4. if HS occurs (i.e. the value for the feature at point 2 is 1), a binary value indicating if the target is a generic group of people (0) or a specific individual (1) (TR column)
5. if HS occurs (i.e. the value for the feature at point 2 is 1), a binary value indicating if the tweeter is aggressive (1) or not (0) (AG column)