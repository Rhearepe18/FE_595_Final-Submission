
import pandas as pd
import numpy as np
import glob
import os
import glob
from textblob import TextBlob


os.chdir('/Users/rhearepe/Downloads/Assignment3')


files = glob.glob('*.txt')
male_data = list()
female_data = list()

def merge_female_files():
    with open('result_female', 'w') as outfile:
        for x in range(1, 20):
            with open(f'female{x}.txt') as infile:
                for line in infile:
                    outfile.write(line)



def merge_male_files():
    with open('result_male', 'w') as outfile:
        for x in range(1, 20):
            with open(f'male{x}.txt') as infile:
                for line in infile:
                    outfile.write(line)


blob_male = list()
sentiment_male = list()
blob_female = list()
sentiment_female = list()

if __name__ == '__main__':

    merge_female_files()
    merge_male_files()
    male_data = [line.strip() for line in open('result_male', 'r')]
    female_data = [line.strip() for line in open('result_female', 'r')]

    for i in (range(0, len(male_data))):
        blob_male.append(TextBlob(male_data[i]))

    for i in range(0, len(blob_male)):
        sentiment_male.append(blob_male[i].sentiment.polarity)

    for i in (range(0, len(female_data))):
        blob_female.append(TextBlob(female_data[i]))

    for i in range(0, len(blob_female)):
        sentiment_female.append(blob_female[i].sentiment.polarity)


male = pd.DataFrame()
pd.set_option('display.max_colwidth', -1)
male['Hero'] = male_data
male['Sentiment Analysis'] = sentiment_male

sort_male = male.sort_values('Sentiment Analysis')
bottom_male = sort_male.head(10)
top_male = sort_male.tail(10)

female = pd.DataFrame()
female['Hero'] = female_data
female['Sentiment Analysis'] = sentiment_female

sort_female = female.sort_values('Sentiment Analysis')
bottom_female = sort_female.head(10)
top_female = sort_female.tail(10)

with open('top_male.txt', 'w') as maletopten:
    maletopten.write(top_male.to_string(header=False, index=False))

with open('bottom_male.txt', 'w') as malebottomten:
    malebottomten.write(bottom_male.to_string(header=False, index=False))

with open('top_female.txt', 'w') as femaletopten:
    femaletopten.write(top_female.to_string(header=False, index=False))

with open('bottom_female.txt', 'w') as femalebottomten:
    femalebottomten.write(bottom_female.to_string(header=False, index=False))


blob = blob_male + blob_female


adjectives = []
count = []

for i in range(0,len(blob)):
    for word, pos in blob[i].tags:
        if pos == 'JJ':
            adjectives.append(word)

for i in range(0,len(adjectives)):
    count.append(adjectives.count(adjectives[i]))

count_top_ten = pd.DataFrame()
count_top_ten['Descriptor'] = adjectives
count_top_ten['Count'] = count

sort_count = count_top_ten.sort_values('Count')
top_descriptors = (sort_count.drop_duplicates().tail(10))

with open('Descriptors.txt', 'w') as descriptors:
    descriptors.write(top_descriptors.to_string(header=False, index=False))
