# Catherine Ann Celeste Quinlan Higher Diploma in Data Analytics Programming project
# Based on Fisher Data set
# Required to investigate and show max,min and mean of each column
# Required to make additional calculations 
# Show some graphs 
# Make some conclusion or inferences from observed data



from urllib.request import urlretrieve              # Alllows importing of data with url 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import statistics

#Stage 1 Data is drawn down and read


df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
df.head()


iris = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'
urlretrieve(iris)
df = pd.read_csv(iris, sep=',')
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = attributes

#Stage 2: Present the data
print(df.head())

#Stage 3: Finding required values, min max and mean  of each column
firstcol = df[:,0]
meanfirstcol = np.mean(df[:,0])
print('mean first column', meanfirstcol) #not working yet

# Stage 4: Show max/min/mean of each iris type using the statistics function imported above
print("minimnums of setosa, virginia and variacolor :")

print("Numer  of setosa, virginia and variacolor iris in the study:")
print(df.groupby('class').size())

print("Average  of attributes for setosa, virginia and variacolor :")

print(df.groupby('class').mean())
 
print("minimnums of attributes for setosa, virginia and variacolor :")
print(df.groupby('class').min())


print("maximums  of attributes for setosa, virginia and variacolor :")
print(df.groupby('class').max())

# Stage 5: Reviewing mean, stand deviation and corrrelation, and predictability

#  Stage 6:  showing graphically that one data type is different using bivariate data (One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. )

