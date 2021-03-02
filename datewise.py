#Hypotheses 2 - choropleth
import pandas as pd
import plotly.express as px


df = pd.read_csv(r'C:\Users\manis\Downloads\novel-corona-virus-2019-dataset (1)\covid_19_data.csv')
print(df)
dfg=df.groupby(['Country/Region', 'ObservationDate'])['Confirmed', 'Deaths', 'Recovered'].sum().reset_index().sort_values('ObservationDate', ascending=True)
print(dfg)

fig = px.choropleth(dfg,locations="Country/Region",locationmode = "country names",
                    color=("Confirmed"),
                    hover_name="Confirmed",
                    animation_frame="ObservationDate")
fig.update_layout(

    title_text='Number of confirmed Covid-19 cases',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ))
fig.show()


