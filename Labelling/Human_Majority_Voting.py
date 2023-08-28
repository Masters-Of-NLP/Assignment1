import pandas as pd


annotated_data = pd.read_csv('Labels/100_labeled_comments.csv')


label_map = {'positive ':'positive'}
annotated_data['20110040']=annotated_data['20110040'].replace(label_map)

annotated_data['Sentiment'] = annotated_data[['20110031','20110040','20110181']].mode(axis=1)[0]

# print(annotated_data)
annotated_data.to_csv('Labels/100_labeled_comments.csv',index=False)