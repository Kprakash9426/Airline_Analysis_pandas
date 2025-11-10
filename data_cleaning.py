# Importing Required Modules
# importing numpy for mathematical operation on arrays and dataframe.

# importing pandas for reading data and data manipualtion.

# importing matplotlib and seaborn to show the insights and visualization from the dataset.

# importing warnings for Warning messages that are typically issued in dataframe where it is useful to alert the user of some condition in a program, where that condition (normally) doesn t warrant raising an exception and terminating the program.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Reading Dataset and Checking the NaN Values , Data Types , and Statistical Analysis
# Since data is in form of excel file we have to use pandas read_excel to load the data

# After loading it is important to check the complete information of data as it can indication many of the hidden infomation such as null values in a column or a row

# Check whether any null values are there or not. if it is present then following can be done,

# Filling NaN values with mean, median and mode using fillna() method Describe data --> which can give statistical analysis

df=pd.read_excel("Data_Train.xlsx")  #Loading excel data
print(df.head()) # Reading the top  5 rows

print(df.info()) #it is useful to get data information like no of rows and colums,non null count,datatype of the columns ,memory used

print("---It is useful to get the statstical information about the dataset----")
df.describe()
df.describe(include=object)
df.describe(include=float)
print(df.describe(include=object))

#to check null values
print("----------displaying the null values count --------")
print(df.isnull().sum())
print(df.shape)

# it returns percentage null values each column in the data frame
df.isnull().sum()/df.shape[0]*100

print("it returns percentage null values each column in the data frame")
print(df.isnull().sum()/df.shape[0]*100)

print("----most frequent values----=---")
print(df['Airline'].mode())

print("__filling  null values using mode function____")
df['Airline']=df['Airline'].fillna(df['Airline'].mode()[0])
print(df['Airline'])

# print(df.isnull().sum())

df['Date_of_Journey'].mode()

print("__filling  null values using mode function____")
df['Date_of_Journey']=df['Date_of_Journey'].fillna(df['Date_of_Journey'].mode()[0])
print(df['Date_of_Journey'])

df['Source'].mode()
df['Source']=df['Source'].fillna(df['Source'].mode()[0])

df['Destination'].mode()
df['Destination']=df['Destination'].fillna(df['Destination'].mode()[0])

df['Route'].mode()
df['Route']=df['Route'].fillna(df['Route'].mode()[0])

df['Dep_Time'].mode()
df['Dep_Time']=df['Dep_Time'].fillna(df['Dep_Time'].mode()[0])

df['Arrival_Time'].mode()
df['Arrival_Time']=df['Arrival_Time'].fillna(df['Arrival_Time'].mode()[0])

df['Duration'].mode()
df['Duration']=df['Duration'].fillna(df['Duration'].mode()[0])

df['Total_Stops'].mode()
df['Total_Stops']=df['Total_Stops'].fillna(df['Total_Stops'].mode()[0])


df['Additional_Info'].mode()
df['Additional_Info']=df['Additional_Info'].fillna(df['Additional_Info'].mode()[0])



df['Price'].mean()
df['Price'].median()


sns.boxplot(df.Price,color="red")
plt.show()

df['Price']=df['Price'].fillna(df['Price'].mean())
print(df.isnull().sum())