import pandas as pd
from quica.quica import Quica

data = pd.read_csv('Labels/100_labeled_comments.csv')

label_map = {'positive':0,'negative':1,'neutral':2}
columns=['20110031','20110040','20110181']
for col in columns:
    data[col]=data[col].map(label_map)

data.drop(columns=['Serial_No','ID','Comment','Sentiment'],inplace=True)
df1 = data[['20110031','20110040']]
df2 = data[['20110040','20110181']]
df3 = data[['20110031','20110181']]


# Krippendroff's alpha to access overall agreement between annotators
alpha_valueb = Quica(dataframe=data).get_results()
print("\n")
print("Overall Agreement Score(Krippendorff's Alpha):")
print(alpha_valueb)
print("\n")

# Krippendroff's alpha between annotator-1(20110031) and annotator-2(20110040)
alpha1 = Quica(dataframe=df1).get_results()
print("Agreement Score b/w annotator-1,2:")
print(alpha1)
print("\n")

# Krippendroff's alpha between annotator-2(20110040) and annotator-3(20110181)
alpha2 = Quica(dataframe=df2).get_results()
print("Agreement Score b/w annotator-2,3:")
print(alpha2)
print("\n")

# Krippendroff's alpha between annotator-1(20110031) and annotator-3(20110181)
alpha3 = Quica(dataframe=df3).get_results()
print("Agreement Score b/w annotator-1,3:")
print(alpha3)