import pandas as pd
import plotly.express as px

# # Read each CSV file into a dataframe
# df_2016 = pd.read_csv('data/world_university_ranking_2016.csv')
# df_2017 = pd.read_csv('data/world_university_ranking_2017.csv')
# df_2018 = pd.read_csv('data/world_university_ranking_2018.csv')
# df_2019 = pd.read_csv('data/world_university_ranking_2019.csv')
# df_2020 = pd.read_csv('data/world_university_ranking_2020.csv')
# df_2021 = pd.read_csv('data/world_university_ranking_2021.csv')
# df_2022 = pd.read_csv('data/world_university_ranking_2022.csv')
# df_2023 = pd.read_csv('data/world_university_ranking_2023.csv')

# year = 2016
# for df in [df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023]:
#     df['year'] = year
#     year += 1

# # Merge all the dataframes into one
# df = pd.concat([df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023])

# # export to csv
# df.to_csv('data/university_ranking_2016_2023.csv', index=False)

# Read the CSV file
df = pd.read_csv('data/university_ranking_2016_2023.csv')

# Create a line chart with plotly.express
fig_linechart = px.line(df, x='year', y='rank', color='name', title='University Ranking by Year')

fig_linechart.update_layout(
    xaxis_title='Year',
    yaxis_title='Rank',
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple",
    ),
    margin=dict(t=30, l=25, r=25, b=25),
)
