import pandas as pd

file1=pd.read_csv('Models/sentiment_output_1.csv')
file2=pd.read_csv('Models/sentiment_output_2.csv')
file3=pd.read_csv('Models/sentiment_output_3.csv')

file2.drop(columns=['ID','Comment','Preprocessed_Comment'],inplace=True)
file3.drop(columns=['ID','Comment','Preprocessed_Comment'],inplace=True)
file1.rename(columns={'Sentiment':'model1'},inplace=True)
file2.rename(columns={'Sentiment':'model2'},inplace=True)
file3.rename(columns={'Sentiment':'model3'},inplace=True)


df = file1.merge(file2, on='Serial_No', how='outer')
merged_df = df.merge(file3,on='Serial_No', how='outer')

def majority_vote(row):
    counts = row.value_counts()
    majority_value = counts.index[0]
    return majority_value

# Apply the majority_vote function to each row and store the result in a new column
merged_df['Sentiment'] = merged_df[['model1', 'model2', 'model3']].apply(majority_vote, axis=1)

merged_df.to_csv('Labels/labeled_comments.csv', index=False)