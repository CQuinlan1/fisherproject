# Catherine Ann Celeste Quinlan Higher Diploma in Data Analytics Programming project
# Based on Fisher Data set
# Required to investigate and show max,min and mean of each column
# Required to make additional calculations 
# Show some graphs 
# Make some conclusion or inferences from observed data



          
import pandas as pd
import numpy 
from matplotlib import pyplot as plt
import seaborn as sns

import statistics

#Stage 1 Data is drawn  from local file  and read

data = numpy.genfromtxt('iris.csv', delimiter=',')


 



iris = 'iris.csv'

df = pd.read_csv(iris, sep=',')
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"] # Headings need to be reinstalled
df.columns = attributes

#Stage 2: Present the data

print("Number  of setosa, virginia and variacolor iris in the study:")
print(df.groupby('class').size())



# Stage 3: Finding the required values of mean of sepal_length,sepal_width,petal_length,petal_width,species
data = numpy.genfromtxt('iris.csv', delimiter=',') # work on datafile saved in same file
# need to round the means of all below to 1 decimal 
sepal_length = (data[:,0])
meanfirstcol = numpy.mean(data[:,0])
roundmeanfirstcol = numpy.round(meanfirstcol,1)
minfirstcol = numpy.min(data[:,0])
maxfirstcol = numpy.max(data[:,0])
print('Mean min and max of sepal_length in the first column is', roundmeanfirstcol,minfirstcol,maxfirstcol)
sepal_width = (data[:,1])
meanseccol = numpy.mean(data[:,1])
roundmeanseccol = numpy.round(meanseccol,1)
minseccol = numpy.min(data[:,1])
maxseccol = numpy.max(data[:,1])
print('Mean min and max of sepal_width in the second column is', roundmeanseccol, minseccol, maxseccol)

petal_length = (data[:,2])
meanthirdcol = numpy.mean(data[:,2])
roundmeanthirdcol = numpy.round(meanthirdcol,1)
minthirdcol = numpy.min(data[:,2])
maxthirdcol = numpy.max(data[:,2])
print('Mean min and max of petal_length in the  third column is', roundmeanthirdcol, minthirdcol, maxthirdcol)


petal_width = (data[:,3])
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
 # st_dev = np.std(data['class'])
 # print("The standard deviation is %r") %(st_dev)

# corr = data.corr()        # correlation of different attributes and we can see if there is a pos correlation
#corr
#  Stage 6:  showing graphically that one data type is different using bivariate data (One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. )


plt.scatter(sepal_length,sepal_width )  # Creates a monotone scatterplot showing sepal length and sepal width
plt.plot()

plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Graph 1 : Scatterplot of Sepal length to Sepal width')
plt.show() 

plt.scatter(petal_length,petal_width )
plt.plot()

plt.xlabel('petal_length')                              # Creates a monotone scatterplot showing Petal length and Petal width
plt.ylabel('petal_width')
plt.title('Graph 2 : Scatterplot of Petal length to Petal width')
plt.show()

# As we can see with these graphs that unless we break them into colour we cannot distinguish any distinction in the patterns their petal and sepal length to width make
iris = sns.load_dataset("iris")

sns.lmplot(x="sepal_length", y="sepal_width", data=iris, hue="species", fit_reg=False, legend=False)  
plt.title(' Graph 3 : Coloured Scatterplot of Sepal length to Sepal width')
plt.legend()
plt.show()



sns.lmplot(x="petal_length", y="petal_width", data=iris, hue="species", fit_reg=False, legend=False)   
plt.title(' graph 4 : Coloured Scatterplot of Petal length to Petal width')
plt.legend()
plt.show()
# Here we plot sepal length divided by width, and petal length divided by width and it will become easier to classify unkown iries from the size catory they fit into

plt.title(' Graph 5 : Coloured Scatterplot of Sepal length divided by  Sepal width')
iris["ID"] = iris.index
iris["ratio of sepal length divided by sepal width"] = iris["sepal_length"]/iris["sepal_width"]
sns.lmplot(x="ID", y="ratio of sepal length divided by sepal width", data=iris, hue="species", fit_reg=False, legend=False)  # Found at https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
plt.legend()
plt.show()

plt.title(' Graph 6 : Coloured Scatterplot of Petal length divided by  Petal width')
iris["ID"] = iris.index
iris["ratio of petal length divided by petal width"] = iris["petal_length"]/iris["petal_width"]
sns.lmplot(x="ID", y="ratio of petal length divided by petal width", data=iris, hue="species", fit_reg=False, legend=False)   # Found at ttps://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
plt.legend()
plt.show()










#plt.figure(figsize=(10,8)) 
# sns.heatmap(corr, 
          #  xticklabels=corr.columns.values,
           # yticklabels=corr.columns.values,
        # cmap='viridis', annot=True)
#plt.show()

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