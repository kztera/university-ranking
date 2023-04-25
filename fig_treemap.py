import plotly.express as px
import numpy as np
import pandas as pd
from add_continent import add_column_continent

df = pd.read_csv("data/world_university_ranking_2023.csv")

add_column_continent(df)

fig = px.treemap(df,
  path=[px.Constant("world"),'continent', 'country'],
  values='number_of_students',
  color='overall_score',
  hover_data=['country', 'number_of_students', 'overall_score'],
  color_continuous_scale='RdBu',
  color_continuous_midpoint=np.average(df['overall_score'], weights=df['number_of_students'])
  )

fig.update_layout(margin = dict(t=30, l=25, r=25, b=25))