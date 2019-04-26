# fisherproject
Python investigation of the Iris data set
This data set I hope to investigate over the next few weeks and break my work on it into steps.
Discuss the background of the data set itself:
    1.  Then using Python, download the csv file
    2.  Present the data in table form.
    3.  Show the min/max/ and mean of each column as required.
    4.  Look at the min/max/mean of each type of iris.
    5.  Graphically represent the dataset.
    6.  Highlight irregularites or similarites.
    7.  Look at standard deviation, correlation and any predictability or inference we might find.
    8.  Summarise findings.
    
    



Summary
Fisher’s Iris Data Set
                                      

The Fisher data set was first introduced in 1936 by Ronald Fisher in a paper he published using it as an example for his study. It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the variation of Iris flowers of three species. 
The Fisher data set consists  of 3 types of data: 50 sample of each of three species of Iris,  setosa, virginica and versicolor, where  4 characteristics noted 
These four features  taken from each sample were: the length and width of  sepals and petals, in centimetres. 
The data set contains 150 observations  (rows of data) of iris flowers. There are four columns of measurements of the flowers . The fifth column is the species of the flower. All observed flowers belong to one of three species.
Central tendency averages
Tables
My program I broke into 6 stages in the end.
My first stage of the program reads the file from a downloaded csv file.
The second stage confirms that we are looking at a balanced set of data where there is 50 studied of each type.


![data iris balanced](https://user-images.githubusercontent.com/47123224/56821672-eaee5c80-6846-11e9-889d-59ea16a50b64.png)

 
Third stage of the program deals with finding the required  values of max/min/mean of sepal_length,sepal_width,petal_length,and petal_width.
![Required min man mean for iris data set](https://user-images.githubusercontent.com/47123224/56820678-74e8f600-6844-11e9-9f78-a8cd5b1e616d.png)

 
Fourth stage I looked at max/min/mean using the numpy function again but of each iris type
![iris data min mxa mean for each iris species](https://user-images.githubusercontent.com/47123224/56820779-ae216600-6844-11e9-9638-8c8069a67c68.png)

 
This I believed allowed for better comparison of the different attributes. We can see that the Setosa data Petal length and petal width set it apart from the others. Also we can note the Virginica sepal length mean at 6.6 . This may have been influenced by an outlier as we can see it has a minimum sepal length equal to that of the versicolor , however it has a maximum sepal length .9 greater.
Stage 5 is where I do some additional statistics calculations  such as  standard deviation, correlation, and covariance 
![siris s devation corr and covariance](https://user-images.githubusercontent.com/47123224/56820860-e1fc8b80-6844-11e9-8d5f-70b4e42c6696.png)

 
We can see that the general standard deviation for all classes for petal length is quite large when compared to the other standard deviations of the data. Also as we had expected the correlation between petal length and petal width, that is, the relationship as petal length increase the width increases is strong and positive at .962314 virtually perfectly linear. The next high correlation I notice is sepal length and petal length at .871283, this is surprising as you would have expected it to have been some strong relationship  between sepal length and width instead but  which are in fact very weakly negatively correlated.
Also worth noting is covariance: between petal length it is highest at 3.096372, while second largest again is sepal length and petal length at 1.270362.
Stage 6 was where I introduced graphics to help me visualise the data. I felt the scatterplot suited the data best. I initially tried with it being monotone but to aid our understanding adapted it to be represented in colour.  I created 6 graphs; the first 2 being monotone so we can compare the effects of colour on our understanding of the data.

![iris graph 1](https://user-images.githubusercontent.com/47123224/56820960-2425cd00-6845-11e9-8254-a8b2fadaf16a.png)
![iris graph 2](https://user-images.githubusercontent.com/47123224/56821084-5fc09700-6845-11e9-9d81-8dac2a8c631f.png)

  
As mentioned until colour is introduced it is difficult to appreciate the data fully.


![iris Graph 3](https://user-images.githubusercontent.com/47123224/56821193-9b5b6100-6845-11e9-9ec6-60211c62554b.png)
![Iris Graph 4](https://user-images.githubusercontent.com/47123224/56821296-cc3b9600-6845-11e9-9b9d-b23b8b234ffa.png)
![iris gaph 5](https://user-images.githubusercontent.com/47123224/56821359-f8efad80-6845-11e9-9212-3e996aca1b77.png)
![iris graph 6](https://user-images.githubusercontent.com/47123224/56821406-23416b00-6846-11e9-9986-c3a7939243e1.png)



 
However, with colour we can easily se that setosa sepal length to sepal width is quite defined whereas there is an overlap in the virginica and versicolor.
 
This graph 4 of petal width to petal length allows us understand our data even more. As expected the longer the petal the wider the petal would be generally. From this visualisation above  we could classify an iris given just petal width to length details with regard to setosa and using certain parameters for these measurements predict into this type of iris category it would go within a certain high degree of accuracy. However, with the overlap of the versicolor and virginica this accuracy would be less in their classification, although up to close where they do overlap we may be able to predict what species it would be .
 
In this graph 5 we can spot an one outlier in the setosa group where sepal length is divided by sepal width. 

In graph 6 we can see that while the ratio of petal length to width   of the species virginica and versicolor are within certain parameters above 2-4 , the ratio for setosa is has much more variance. It can be seen from the graph to be between 2.5 to greater than 14 .

Conclusion: 
•	Setosa variety can be easily classified just by petal length and width, or sepal width and sepal length 
•	With better parameters we could with varying degree of certainty classify the virginica and versicolor given their petal length and petal width
•	There is a very strong positive correlation between the irises ‘ petal width and petal length as expected  however also interestingly very strong positive correlation between sepal length and petal length

This has been a very interesting and enjoyable project. It allows us  note that the setosa data type due to its smaller petal length and width  which creates its own cluster as in graph 3 or separate group as in 4, and  is easier to classify within a certain high degree of accuracy compared to the other two types versicolor and virginica,  However with the other two types it would be quite difficult and varies along their size parameters however, where they overlap (as in graph 4 where petal length is between 4.5 -5.5) it becomes impossible to class them accurately, also we saw their ratio of petal length to width are very  similar as are sepal length to sepal width and does not vary as the setosa’s. Perhaps understanding that virginica’s petal width and  length are the largest and when given these measurements as groupings the higher they are the easier and more accurate it is to classify the iris as a virginica. So within certain parameter sizes or size category grouping I believe we would have a higher confidence of categorising it into a certain iris type with further study.
Also worth noting is the relationship between petal length and sepal length which could lead to other investigations.

.




 

References:
https://www.kaggle.com/mjbahmani/20-ml-algorithms-15-plot-for-beginners
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
https://www.youtube.com/watch?v=FLuqwQgSBDw
https://courses.cs.ut.ee/MTAT.03.183/2017_spring/uploads/Main/example_submission.html
http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html

![data iris balanced](https://user-images.githubusercontent.com/47123224/56813531-0ea8a700-6835-11e9-99fb-6d059148886d.png)

