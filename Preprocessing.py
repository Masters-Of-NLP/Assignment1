import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Initialize stop words for English
stop_words = set(stopwords.words('english'))

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()


# Preprocess the comment.
def preprocess_comment(comment):
    comment = str(comment)
    # Tokenize the text
    tokens = word_tokenize(comment)
    
    # Lemmatize, remove stop words, and convert to lowercase
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    # Join back into a string
    return ' '.join(tokens)


# Read the csv file
comments = pd.read_csv('Comments_Scraped/comments.csv')

# Drop the index and meta-data columns
comments.drop(comments.columns[0],axis=1,inplace=True)
comments.drop(comments.columns[2:5],axis=1,inplace=True)

# Remove null value comments, if any
comments.dropna(inplace=True)
comments['Preprocessed']=comments['comment']


# Pre-processing the comments to acheive the following points:
#   1. Removing the URLs using standard patterns like https, http, r/
#   2. Removing special characters other than periods and commas
#   3. Converting into lowercase
#   4. Only handling the english comments using ASCII range
#   5. Removing any characters that are not word characters, spaces or periods
#   6. Removing any extra spaces between two words
for index, row in comments.iterrows():
    text = row["Preprocessed"]
    url_pattern = r'https\S*|http\S*|www\.\S*|r/\S*'
    cleaned = re.sub(url_pattern, r'', text)
    cleaned = re.sub(r'[?|!|\'|"|#|%|$|@|*|(|)|\-|_|=|+]', r' ', cleaned)
    cleaned = cleaned.lower()
    cleaned = re.sub(r'[^\x00-\x7F]+', ' ', cleaned)
    cleaned = re.sub(r'(?<!\d)\.(?!\d)', ' ', cleaned)  # This preserves only decimal points
    cleaned = re.sub(r'[^\w\s.]', ' ', cleaned)
    cleaned = ' '.join(cleaned.split())
    comments.at[index, "Preprocessed"] = cleaned

# Apply preprocessing to the comments
comments['Preprocessed'] = comments['Preprocessed'].apply(preprocess_comment)

# Removing any comments that have only spaces and no meaningful words
comments = comments[comments['Preprocessed'].str.strip().notna() & (comments['Preprocessed'].str.strip() != '')]
comments.dropna(inplace=True)

# Reseting index
comments.reset_index(drop=True,inplace=True)
comments.insert(0,'Sr No.',range(1,1+len(comments)))

# Save the preprocessed comments to a CSV file
comments.to_csv('preprocessed_comments.csv', index=False)  # Change the path accordingly

