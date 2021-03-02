#Hypotheses 3
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\manis\Desktop\unt sundar\5709\project2\final_aqi_df.csv')
dfgroup=df.groupby(['country'])

dfspain=dfgroup.get_group('Spain')
dfitaly=dfgroup.get_group('Italy')
dfindia=dfgroup.get_group('India')
dfgermany=dfgroup.get_group('Germany')


dfspain.plot( x='week',y=['NO2','PM2.5'],kind='line')
plt.axvline(11,linestyle='--',color='black',label='lockdown week')
plt.title('Pollutant levels in Spain from 1st - 14th week of 2020')
plt.ylabel('Levels of NO2 and PM2.5')
plt.legend()
plt.show()

dfitaly.plot( x='week',y=['NO2','PM2.5'],kind='line')
plt.axvline(11,linestyle='--',color='black',label='lockdown week')
plt.title('Pollutant levels in Italy from 1st - 14th week of 2020')
plt.ylabel('Levels of NO2 and PM2.5')
plt.legend()
plt.show()

dfindia.plot( x='week',y=['NO2','PM2.5'],kind='line')
plt.axvline(12,linestyle='--',color='black',label='lockdown week')
plt.title('Pollutant levels in India from 1st - 14th week of 2020')
plt.ylabel('Levels of NO2 and PM2.5')
plt.legend()
plt.show()



dfgermany.plot( x='week',y=['NO2','PM2.5'],kind='line')
plt.axvline(13,linestyle='--',color='black',label='lockdown week')
plt.title('Pollutant levels in Germany from 1st - 14th week of 2020')
plt.ylabel('Levels of NO2 and PM2.5')
plt.legend()
plt.show()