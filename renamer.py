import pandas as pd

data = pd.read_csv("Dataset.csv")

print(data.head())

data['value'] = data['sentiment'].map({'positive': 1, 'negative': 0})

# data.loc[data.sentiment != 'positive', 'positive'] = 1
# # w.loc[w.female == 'female', 'female'] =

data = data.drop(['sentiment'],axis=1)


#
# print(data['sentiment'])
print(data.head())

# d


data.to_csv("review.csv", sep='\t')