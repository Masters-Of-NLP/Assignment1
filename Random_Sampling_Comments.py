# Importing libraries
import pandas as pd

# Read the final labeled comments file
comments=pd.read_csv('Labels/labeled_comments.csv')

# Random sampling of comments
samples_per_group = 100//3

def sample_group(group):
    return group.sample(n=samples_per_group, replace=True)

sampled_comments = comments.groupby('Sentiment', group_keys=False, as_index=False).apply(sample_group)

sampled_indices = set(sampled_comments.index)
remaining_comments = comments[~comments.index.isin(sampled_indices)]
additional_sample = remaining_comments.sample(n=1)

sampled_comments = pd.concat([sampled_comments, additional_sample], ignore_index=True)
sampled_comments = sampled_comments.drop(columns=['model1','model2','model3','Sentiment','Preprocessed_Comment'])
sampled_comments.to_csv('Comments_Scraped/100_sampled_comments.csv', index=False)