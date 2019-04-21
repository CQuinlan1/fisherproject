# Catherine Ann Celeste Quinlan Higher Diploma in Data Analytics Programming project
# Based on Fisher Data set
# Required to investigate and show max,min and mean of each column
# Required to make additional calculations 
# Show some graphs 
# Make some conclusion or inferences from observed data



          
import pandas as pd
import numpy 
import matplotlib.pyplot as plt
import seaborn as sns

import statistics

#Stage 1 Data is drawn down and read

data = numpy.genfromtxt('iris.csv', delimiter=',')


 



iris = 'iris.csv'

df = pd.read_csv(iris, sep=',')
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"] # Headings need to be reinstalled
df.columns = attributes

#Stage 2: Present the data

print("Number  of setosa, virginia and variacolor iris in the study:")
print(df.groupby('class').size()) #"\n" drop to next line 


# Stage 3: Finding the required values of mean of sepal_length,sepal_width,petal_length,petal_width,species
data = numpy.genfromtxt('iris.csv', delimiter=',') # work on datafile saved in same file
# need to round the means of all below to 1 decimal 
meanfirstcol = numpy.mean(data[:,0])
roundmeanfirstcol = numpy.round(meanfirstcol,1)
minfirstcol = numpy.min(data[:,0])
maxfirstcol = numpy.max(data[:,0])
print('Mean min and max of sepal_length in the first column is', roundmeanfirstcol,minfirstcol,maxfirstcol)
seccol = data[:,1]
meanseccol = numpy.mean(data[:,1])
roundmeanseccol = numpy.round(meanseccol,1)
minseccol = numpy.min(data[:,1])
maxseccol = numpy.max(data[:,1])
print('Mean min and max of sepal_width in the second column is', roundmeanseccol, minseccol, maxseccol)

thirdcol = data[:,2]
meanthirdcol = numpy.mean(data[:,2])
roundmeanthirdcol = numpy.round(meanthirdcol,1)
minthirdcol = numpy.min(data[:,2])
maxthirdcol = numpy.max(data[:,2])
print('Mean min and max of petal_length in the  third column is', roundmeanthirdcol, minthirdcol, maxthirdcol)


fourthcol = data[:,3]
meanfourthcol = numpy.mean(data[:,3])
roundmeanfourthcol = numpy.round(meanfourthcol,1)
minfourthcol = numpy.min(data[:,3])
maxfourthcol = numpy.max(data[:,3])
print('Mean min and max of petal_width in the  fourth  column is',roundmeanfourthcol, minfourthcol, maxfourthcol)


# Stage 4: Show max/min/mean of each iris type using the statistics function imported above




print("Average/mean  of attributes for setosa, virginia and variacolor :")

print(numpy.round(df.groupby('class').mean(),1)) #  rounding the means to 1 decimal
 
print("minimnums of attributes for setosa, virginia and variacolor :")
print(df.groupby('class').min())


print("maximums  of attributes for setosa, virginia and variacolor :")
print(df.groupby('class').max())

# Stage 5: Reviewing mean, stand deviation and corrrelation, and predictability
 # st_dev = np.std(data['alcohol'])
 # print("The standard deviation is %r") %(st_dev)

# corr = data.corr()        # correlation of different attributes and we can see if there is a pos correlation
#corr
#  Stage 6:  showing graphically that one data type is different using bivariate data (One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. )

plt.plot(kind = 'scatter', x ='sepal_length', y = 'sepal_width')
plt.show()   

#plt.figure(figsize=(10,8)) 
# sns.heatmap(corr, 
          #  xticklabels=corr.columns.values,
           # yticklabels=corr.columns.values,
        # cmap='viridis', annot=True)
#plt.show()