import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mymoviedb.csv', lineterminator='\n')

# df.info()

#print(df.describe())

df['Release_Date'] = pd.to_datetime(df['Release_Date'])
#print(df['Release_Date'].dtype)

df['Release_Date'] = df['Release_Date'].dt.year
#print(df['Release_Date'].dtype)

cols = ['Overview', 'Original_Language', 'Poster_Url']
df.drop(cols, axis=1, inplace=True)

# print(df.head())

#catigorizing Vote_Averahe into Popular,Average,Belo Average,Poor by creating function

def catigorize_col(df, col, lables):
    
    #setting edge to cut the column
    edges = [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ]

    df[col] = pd.cut(df[col], edges, labels=lables, duplicates='drop')
    return df

#define lables
lables = ['Not_Popular', 'Below_Avg', 'Average', 'Popular']

#catigeorize on basis of lable
catigorize_col(df, 'Vote_Average', lables)

#comfirming changes
df['Vote_Average'].unique()
# print(df.head())

#droping na values
df.dropna(inplace=True)

#confirming it
df.isna().sum()

#now spliting the genes colums for each movie in new line.
# ie spiderman have Action, Drama, Romance genes....... now we are spliting it into..... 
# spiderman.......Drama
# spiderman.......Action
# spiderman.......Romance

#spliting
df['Genre'] = df['Genre'].str.split(', ')

#exploding to new line
df = df.explode('Genre').reset_index(drop=True)
# print(df.head())

#converting dtype of genre to catogery
df['Genre'] = df['Genre'].astype('category')
#confirm changes
# print(df['Genre'].dtypes)

# print(df.info())


#Data Visualization
#using matplotlib and seaborn

#setting up seaborn configuration
sns.set_style('whitegrid')

#Q1 What is the most frequent genre in the dataset?
#showning stats on genre column
df['Genre'].describe()

#ploting graph
# sns.catplot(y='Genre', data=df, kind='count',
#             order=df['Genre'].value_counts().index)
# plt.title('Genre column distribution')
# plt.show()


#Q2: What genres has highest votes ?
# sns.catplot(y='Vote_Average', data=df, kind='count',
#             order=df['Vote_Average'].value_counts().index)
# plt.title('Vote Count')
# plt.show()


#Q3: What movie got the highest popularity ? what's its genre ?
# print(df[df['Popularity'] == df['Popularity'].max()])


#What movie got the lowest popularity? what's its genre?
#print(df[df['Popularity'] == df['Popularity'].min()])

#Q5: Which year has the most filmmed movies?
df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()


"""
Summary

Q1: What is the most frequent genre in the dataset?
Drama genre is the most frequent genre in our dataset and has appeared more than
14% of the times among 19 other genres.

Q2: What genres has highest votes ?
we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the
highest popularity among fans by being having more than 18.5% of movies popularities.

Q3: What movie got the highest popularity ? what's its genre ?
Spider-Man: No Way Home has the highest popularity rate in our dataset and it has
genres of Action , Adventure and Sience Fiction .

Q4: What movie got the lowest popularity ? what's its genre ?
The united states, thread' has the highest lowest rate in our dataset
and it has genres of music , drama , 'war', 'sci-fi' and history`.

Q5: Which year has the most filmmed movies?
year 2020 has the highest filmming rate in our dataset.

"""
