from dash import Dash, dcc, html
import plotly.express as px
from test import fig
'''
dash.Dash: The Application
dash.dcc: Interactive Components
dash.html: HTML Tags
'''
import pandas as pd

# Load Data
data_2023 = pd.read_csv("data_2023.csv")
data_2022 = pd.read_csv("data_2022.csv")

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
        # html.P(children="📊", className="header-emoji"),
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
    dcc.Graph(
      id="my-graph",
      figure=fig
    )
  ]
)

if __name__ == "__main__":
  app.run_server(debug=True)