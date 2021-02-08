# Adolescent fertility Analysis

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Adolescent Fertility Analysis Report](#adolescent-fertility-analysis-report)
- [Data Sources](#data-sources)


## Background

Approximately 16 million young people aged 15-19 give birth each year, accounting for approximately 11% of all production in the world. 95% of this production occurs in low- and middle-income countries. The average productivity of young people in middle-income countries is more than double that of high-income countries, and the rate in low-income countries is four times higher.


## Install

Environment

```
Python 3.7.7
```

Clone the git repo, then install the requirements with pip

```
git clone https://git.esiee.fr/guanji/adolescent-fertility-analysis.git
cd adolescent-fertility-analysis
pip install -r requirements.txt
```


## Usage

Run the app 

```
python app.py
```


myClass.py<br/>

myClass.py is for data processing.<br/>


4 founctions:<br/>

initializeDataframe : This function is to simply initialize the dataframe. The CSV file contains some useless rows, so we need to delete them and set the column names.<br/>

changeStru : This function is to change the structure of the dataframe. We need a "tidy" data structure: each variable is a column, each observation is a row.<br/>

getDataframe : Use this function to call the initializeDataframe function and the changeStru function to avoid heavy code.<br/>

uniteDataframe : In order to display the data more clearly and quickly, we can combine the two dataframes. And because each data file contains different countries with data, we need to do some filtering to keep the same country data.
<br/>


## Adolescent Fertility Analysis Report


### Adolescent fertility : Why?


Approximately 16 million young people aged 15-19 give birth each year, accounting for approximately 11% of all production in the world. 95% of this production occurs in low- and middle-income countries. The average productivity of young people in middle-income countries is more than double that of high-income countries, and the rate in low-income countries is four times higher.

#### Distribution of Adolescent fertility

 &nbsp;         
    
![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_7_1.png)
    
 &nbsp;         
 
![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_10_1.png)
    

 &nbsp;         
   

From the distribution chart above, we can see that 2018 is the best. And adolescent fertility is a difficult problem to solve, because there is almost no difference in the data distribution from 2014 to 2018. Fortunately, most of the distribution area is in the low-value area.

    
 &nbsp;         
    

#### What Influences adolescent fertility?

The UN report pointed out that Adolescent fertility is a common problem in high-income, middle-income and low-income countries. However, around the world, marginalized communities are more likely to have Adolescent fertility, usually due to poverty, lack of education and employment opportunities.   

    

    

##### Adolescent fertility VS GDP

&nbsp; 

![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_22_1.png)
    
&nbsp;          

It is very clear that the ratio of adolescent fertility is higher in low-income countries, and the situation between high-income and middle-income countries is similar. There are even some middle-income countries that perform better than high-income countries

     

##### Adolescent fertility VS Education

&nbsp;  
    
![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_28_0.png)
    
 &nbsp;         

Picture above confirms that, secondary school enrollment and Adolescent fertility depicts linear relation with positive correlation. 

     

##### Adolescent fertility VS Labor force female

 &nbsp;         
    
![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_35_1.png)
    


    

According to the above picture, we can confirm that the relationship between female employment opportunities and adolescent fertility is not very close.

    

### Conclusion

    

Education is having highest impact on adolescent fertility. Female employment opportunities is having least impact on Happiness Score.
All in all, the order of importance is education > GDP > female employment opportunities.
Fortunately, in the past two to three decades, the adolescent fertility rate in most countries and regions has dropped significantly. The education level received by girls in most countries has risen, and employment opportunities have expanded. Low level of education is closely related to early birth.

     

### Map

 &nbsp;         
    
![png](Adolescent%20Fertility%20Analysis%20Report_files/Adolescent%20Fertility%20Analysis%20Report_47_1.png)



## Data Sources

Adolescent fertility : https://data.worldbank.org/indicator/SP.ADO.TFRT?view=chart<br/>
GDP : https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?view=chart<br/>
Secondary school enrollment : https://data.worldbank.org/indicator/SE.SEC.ENRR?view=chart<br/>
Labor force female : https://data.worldbank.org/indicator/SL.TLF.TOTL.FE.ZS?view=chart<br/>





