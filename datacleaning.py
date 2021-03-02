#data cleaning, EDA, and Hypotheses1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from matplotlib import cm
df = pd.read_csv(r'C:\Users\manis\PycharmProjects\5709project\5709Project.csv')


#removed continents
df=df[df['Country,Other']!='World']
df=df[df['Country,Other']!='\nNorth America\n']
df=df[df['Country,Other']!='\nEurope\n']
df=df[df['Country,Other']!='\nAsia\n']
df=df[df['Country,Other']!='\nSouth America\n']
df=df[df['Country,Other']!='\nOceania\n']
df=df[df['Country,Other']!='\nAfrica\n']
df=df[df['Country,Other']!='\n\n']



#removed unnecessary columns
df = df.drop('NewCases', axis=1)
df = df.drop('NewDeaths', axis=1)
#Data cleaning
df = df.rename(columns={'Serious,Critical': 'Serious', 'Tot Cases/1M pop': 'Total Cases per 1M Pop', 'Deaths/1M pop':'Deaths per 1M Pop','Tests/\n1M pop\n': 'Tests per 1M Pop'})
df = df.fillna(0)
print(df)
#df = df.drop(df.index[211])
df["TotalCases"] = df["TotalCases"].str.replace(",","").astype(float)
df["TotalDeaths"] = df["TotalDeaths"].str.replace(",","")
df["TotalDeaths"] = df["TotalDeaths"].replace(" ",0)
df["TotalDeaths"] = pd.to_numeric(df["TotalDeaths"], downcast="float")

df["TotalTests"] = df["TotalTests"].str.replace(",","")
df["TotalTests"] = pd.to_numeric(df["TotalTests"], downcast="float")
df=df.fillna(0)

df['TotalRecovered'] = df['TotalRecovered'].str.replace(",","")
df["TotalRecovered"] = pd.to_numeric(df["TotalRecovered"], downcast="float")
df=df.fillna(0)

df['ActiveCases'] = df['ActiveCases'].str.replace(",","")
df["ActiveCases"] = pd.to_numeric(df["ActiveCases"], downcast="float")
df=df.fillna(0)

df['Serious'] = df['Serious'].str.replace(",","")
df["Serious"] = pd.to_numeric(df["Serious"], downcast="float")
df=df.fillna(0)

df['Total Cases per 1M Pop'] = df['Total Cases per 1M Pop'].str.replace(",","")
df["Total Cases per 1M Pop"] = pd.to_numeric(df["Total Cases per 1M Pop"], downcast="float")
df=df.fillna(0)

df['Deaths per 1M Pop'] = df['Deaths per 1M Pop'].str.replace(",","")
df['Deaths per 1M Pop'] =pd.to_numeric(df['Deaths per 1M Pop'],downcast='float')
df=df.fillna(0)
df['Tests per 1M Pop'] = df['Tests per 1M Pop'].str.replace(",","")
df["Tests per 1M Pop"] = pd.to_numeric(df["Tests per 1M Pop"], downcast="float")
df=df.fillna(0)
df.at[13,'TotalRecovered']=344
#data analysis
df['Positivepercentage']=((df['TotalCases'])/df['TotalTests'])*100
df['Positivepercentage']=df['Positivepercentage'].replace(np.inf,0)

df['RecoveredPercentage']=((df['TotalRecovered'])/df['TotalCases'])*100
df['DeathPercentage']=((df['TotalDeaths'])/df['TotalCases'])*100

df = df.sort_values('TotalCases',ascending=False)
df1=df.loc[df["TotalCases"] > 1000]




d_color = cm.viridis_r(np.linspace(.4, .8, 30))
r_color = cm.magma_r(np.linspace(.4, .8, 30))
c_color = cm.inferno_r(np.linspace(.4, .8, 30))

#Bar chart
df1.groupby("Country,Other").DeathPercentage.max().sort_values(ascending=False)[:25].plot.bar(color=d_color)
plt.title("Top 25 countries with highest Death Percentage whose total cases are greater than 1000")
plt.xlabel("Country")
plt.ylabel("Death Percentage")

plt.show()
df1.groupby("Country,Other").RecoveredPercentage.max().sort_values(ascending=False).tail(25).plot.bar(color=r_color)
plt.title("Countries(25) with lowest Recovered Percentage whose total cases are greater than 1000")
plt.xlabel("Country")
plt.ylabel("Recovered Percentage")
plt.show()
df1.groupby("Country,Other").Positivepercentage.max().sort_values(ascending=False)[:25].plot.bar(color=c_color)
plt.title("Top 25 countries with highest confirmed percentage whose total cases are greater than 1000")
plt.xlabel("Country")
plt.ylabel("Confirmed Percentage")
plt.show()


#Box plot
sb.boxplot('Continent','Total Cases per 1M Pop',data=df).set_title("Box Plot of confirmed cases per 1M Population")
plt.show()
sb.boxplot('Continent','Deaths per 1M Pop',data=df).set_title("Box Plot of Deaths per 1M Population")
plt.show()

dfgroup=df.groupby(['Continent'])
dfeurope=dfgroup.get_group('Europe')
dfNA=dfgroup.get_group('North America')
dfasia=dfgroup.get_group('Asia')


#histogram
fig=plt.figure(figsize=(13,10))
europe=fig.add_subplot(1,2,1)
na=fig.add_subplot(1,2,2)
europe.hist(dfeurope['Total Cases per 1M Pop'],color='blue',bins=30)
europe.set_xlabel('Total Cases per 1M Pop')
europe.set_ylabel('Number of Countries')
europe.set_title('Histogram of the Distribution of total cases per 1million in europe')
na.hist(dfNA['Total Cases per 1M Pop'],color='red',bins=30)
na.set_xlabel('Total Cases per 1M Pop')
na.set_ylabel('Number of Countries')
na.set_title('Histogram of the Distribution of total cases per 1 million in North America')
plt.show()

fig1=plt.figure(figsize=(13,10))
europe=fig1.add_subplot(1,2,1)
na=fig1.add_subplot(1,2,2)
europe.hist(dfeurope['Deaths per 1M Pop'],color='blue',bins=30)
europe.set_xlabel('Deaths per 1M Pop')
europe.set_ylabel('Number of Countries')
europe.set_title('Histogram of the Distribution of deaths per 1million in europe')
na.hist(dfNA['Deaths per 1M Pop'],color='red',bins=30)
na.set_xlabel('Deaths per 1M Pop')
na.set_ylabel('Number of Countries')
na.set_title('Histogram of the Distribution of deaths per 1 million in North America')
plt.show()

x = pd.DataFrame(df).to_csv('5709FinalProject.csv', header=True, index=None)

