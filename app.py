from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from fig_treemap import *
from fig_line_chart import *
from add_continent import add_column_continent
'''
dash.Dash: The Application
dash.dcc: Interactive Components
dash.html: HTML Tags
'''
import pandas as pd

# Load Data
data_2023 = pd.read_csv("data\world_university_ranking_2023.csv")
data_2022 = pd.read_csv("data\world_university_ranking_2022.csv")
data_2016_2023 = pd.read_csv("data/university_ranking_2016_2023.csv")

# data
add_column_continent(data_2022)
add_column_continent(data_2023)

uni_names = data_2016_2023['name'].unique()
continents = ['world', 'Africa', 'Asia', 'Australia', 'Europe', 'North America', 'South America']
years = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
treemap_allocation_choice = ["number_of_students", "overall_score", "teaching_score", "research_score",	"citations_score",	"industry_income_score", "international_outlook_score"]
treemap_with_choice = ["overall_score", "teaching_score", "research_score",	"citations_score",	"industry_income_score", "international_outlook_score"]
linechart_sort_by = ["rank", "number_of_students", "overall_score", "teaching_score", "research_score",	"citations_score",	"industry_income_score", "international_outlook_score"]
'''
Columns of the Data:
  - rank: xếp hạng của trường đại học
  - name: tên của trường đại học
  - country: quốc gia của trường đại học
  - number_of_students: số lượng sinh viên
  - student_per_staff: số lượng sinh viên trên mỗi giáo viên
  - international_students: phần trăm sinh viên quốc tế
  - female_male_ratio: tỉ lệ sinh viên nữ / nam
  - overall_score: điểm tổng thể
  - teaching_score: điểm giảng dạy
  - research_score: điểm nghiên cứu
  - citations_score: điểm trích dẫn
  - industry_income_score: điểm thu nhập từ ngành công nghiệp
  - international_outlook_score: điểm quan điểm quốc tế
'''

external_stylesheets = [
  {
    "href": (
      "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap"
      ),
    "rel": "stylesheet",
  }
]

image_path = 'assets/logo.png'


# Create Application
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "World University Rankings 2022 - 2023"

# Create Layout
app.layout = html.Div(
  children=[
    html.Div(
      children=[
        html.Img(
          src=r'assets/logo.png',
          style={
            'height': '35%'
          },
          className="center"
        ),
        html.H1(
          children="World University Rankings",
          className="header-title",
        ),
        html.Br(),
        html.P(
          children=" The largest and most diverse university rankings to date include 1,799 universities across 104 countries and regions by The Times Higher Education.",
          className="header-description",
        ),
      ],
      className="header",
    ),
    html.Div(
      children=[
        html.Div(
            children=[
                html.Div(children="Continent", className="menu-title"),
                dcc.Dropdown(
                    id="continent-filter",
                    options=[
                      {"label": continent, "value": continent}
                      for continent in continents
                    ],
                    searchable=False,
                    value=[],
                    className="dropdown",
                    multi=True
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(children="Allocation by", className="menu-title"),
                dcc.Dropdown(
                    id="allocation-by-filter",
                    options=[
                      {
                        "label": choice,
                        "value": choice
                      } for choice in treemap_allocation_choice
                    ],
                    searchable=False,
                    value="number_of_students",
                    className="dropdown",
                    clearable=False
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children="With", className="menu-title"
                ),
                dcc.Dropdown(
                  id="color-filter",
                  options=[
                      {
                        "label": choice,
                        "value": choice
                      } for choice in treemap_with_choice                
                  ],
                  value="overall_score",
                  searchable=False,
                  clearable=False,
                  className="dropdown",
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children="Year", className="menu-title"
                ),
                dcc.Dropdown(
                  id="year-filter",
                  options=[
                    {
                      "label": year,
                      "value": year
                    } for year in years
                  ],
                  value=2023,
                  clearable=False,
                  searchable=False,
                  className="dropdown",
                ),
            ]
        ),
    ],
    className="menu",
  ),
  dcc.Graph(
    id="my-graph",
    figure=fig,
    className='graph treemap'
  ),
  html.Div(
    children=[
      html.P(
        children=[
            html.Br(),
            html.P(
              children="University Ranking by Year",
              className="title-chart",
            ),
        ]
      )
    ],
    className="title-container",
  ),
  html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children="University name", className="menu-title"),
                dcc.Dropdown(
                    id="name-filter",
                    options=[
                      {"label": name, "value": name}
                      for name in uni_names
                    ],
                    clearable=True,
                    value=['Massachusetts Institute of Technology', 'Stanford University', 'University of Oxford'],
                    className="dropdown",
                    multi=True
                ),
            ]
        ),
        html.Div(
          children=[
            html.Div(children="Sort by", className="menu-title"),
            dcc.Dropdown(
              id="sort-by-filter",
              options=[
                {"label": choice, "value": choice}
                for choice in linechart_sort_by
              ],
              value="rank",
              searchable=False,
              clearable=False,
              className="dropdown",
            )
          ]
        ),
        html.Div(
            children=[
                html.Div(children="Start year", className="menu-title"),
                dcc.Dropdown(
                    id="start-year-filter",
                    options=[
                      {
                        "label": year,
                        "value": year
                      } for year in years
                    ],
                    value=2016,
                    searchable=False,
                    className="dropdown",
                    clearable=False
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children="End year", className="menu-title"
                ),
                dcc.Dropdown(
                  id="end-year-filter",
                  options=[
                      {
                        "label": year,
                        "value": year
                      } for year in years
                  ],
                  value=2023,
                  searchable=False,
                  clearable=False,
                  className="dropdown",
                ),
            ],
        ),
    ],
    className="menu container",
  ),
  html.Div(
    children=[
      dcc.Graph(
        id="my-graph-2",
        figure=fig_linechart,
        className='graph linechart'
      ),
    ],
    className="linechart",
  ),
  ],
)

@app.callback(
  Output("my-graph", "figure"),
  [Input("continent-filter", "value")],
  Input("allocation-by-filter", "value"),
  Input("color-filter", "value"),
  Input("year-filter", "value"),
)

def update_charts(continent, allocation, colorFilter, year):
  df = pd.read_csv(f'data/world_university_ranking_{year}.csv')
  add_column_continent(df)
  if continent == [] or continent == ['world'] or 'world' in continent:
    fig = px.treemap(
      df,
      path=[px.Constant("world"),'continent', 'country'],
      values=allocation,
      color=colorFilter,
      hover_data=['country', f'{allocation}', f'{colorFilter}'],
      color_continuous_scale='RdBu',
      template='plotly_white',
      color_continuous_midpoint=np.average(df[f'{colorFilter}'], weights=df[f'{allocation}'])
  )
  else:
    fig = px.treemap(
      df[df['continent'].isin(continent)],
      path=[px.Constant('world'),'continent','country'],
      values=allocation,
      color=colorFilter,
      hover_data=['country', f'{allocation}', f'{colorFilter}'],
      color_continuous_scale='RdBu',
      color_continuous_midpoint=np.average(df[f'{colorFilter}'], weights=df[f'{allocation}'])
  )
  fig.update_layout(margin = dict(t=30, l=25, r=25, b=25))
  return fig

@app.callback(
  Output("my-graph-2", "figure"),
  [Input("name-filter", "value")],
  Input("sort-by-filter", "value"),
  Input("start-year-filter", "value"),
  Input("end-year-filter", "value"),
)

def update_charts_2(name, sort_by, start_year, end_year):
  year = [i for i in range(start_year, end_year+1)]
  if name == []:
    fig_linechart = px.line(data_2016_2023, x='year', y='rank', color='name', hover_data=['name', 'rank', 'year'], color_discrete_sequence=px.colors.qualitative.Pastel, template='plotly_white',)
  else:
    df = data_2016_2023[data_2016_2023['name'].isin(name) & data_2016_2023['year'].isin(year)]
    fig_linechart = px.line(df, x='year', y=f'{sort_by}', color='name', markers=True, hover_data=["rank", "number_of_students", "overall_score", "teaching_score", "research_score",	"citations_score",	"industry_income_score", "international_outlook_score", "year"], color_discrete_sequence=px.colors.qualitative.Pastel, template='plotly_white', symbol='name') 
    # fig_linechart = px.line(df, x='year', y='rank', color='name', markers=True, hover_data=['name', 'rank', 'year'], color_discrete_sequence=px.colors.qualitative.Pastel, template='plotly_white', symbol='name')

  fig_linechart.update_layout(
    xaxis_title='Year',
    yaxis_title=f'{sort_by}',
    font=dict(
        family="Lato, sans-serif",
        size=14,
    ),
    margin=dict(t=30, l=25, r=25, b=25),
  )
  return fig_linechart

if __name__ == "__main__":
  app.run_server(debug=True)