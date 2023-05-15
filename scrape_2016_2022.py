import pandas as pd
import numpy as np

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service = Service(executable_path=EdgeChromiumDriverManager().install())

year = 2016

while (year < 2023):
  url_stats = f'https://www.timeshighereducation.com/world-university-rankings/{year}/world-ranking#!/page/0/length/-1/sort_by/rank/sort_order/asc/cols/stats'

  url_score = f'https://www.timeshighereducation.com/world-university-rankings/{year}/world-ranking#!/page/0/length/-1/sort_by/rank/sort_order/asc/cols/scores'

  web_driver_stats = webdriver.ChromiumEdge(service=service)
  web_driver_stats.get(url_stats)

  # Đợi cho đến khi tất cả các phần tử được tải
  web_driver_stats.implicitly_wait(10)

  # Lấy code HTML của trang web
  stats_html = web_driver_stats.page_source

  # Parse HTML
  stats_soup = bs(stats_html, 'html.parser')

  # Lấy các đối tượng cần thiết
  uni_stats_rank = stats_soup.find_all('td', {'class':'rank sorting_1 sorting_2'})
  uni_name = stats_soup.find_all(name=["a", "div"], attrs={"class": "ranking-institution-title"})
  uni_location = stats_soup.findAll("div", {"class":"location"})
  uni_stats_number_students = stats_soup.findAll("td", {"class":"stats stats_number_students"})
  uni_stats_students_per_staff = stats_soup.findAll("td", {"class":"stats stats_student_staff_ratio"})
  uni_stats_international_students = stats_soup.findAll("td", {"class":"stats stats_pc_intl_students"})
  uni_stats_female_male_ratio = stats_soup.findAll("td", {"class":"stats stats_female_male_ratio"})

  # Đóng trình duyệt
  web_driver_stats.close()

  # Score
  web_driver_score = webdriver.ChromiumEdge(service=service)

  web_driver_score.get(url_score)

  # Đợi cho đến khi tất cả các phần tử được tải
  web_driver_score.implicitly_wait(10)

  # Lấy code HTML của trang web
  score_html = web_driver_score.page_source

  # Parse HTML
  score_soup = bs(score_html, 'html.parser')

  # Lấy các đối tượng cần thiết
  # Vì thứ tự của các trường giống với `rank` nên ta chỉ cần bắt đầu lấy từ cột thứ 3
  uni_overall_score = score_soup.findAll("td", {"class":"scores overall-score"})
  uni_teaching_score = score_soup.findAll("td", {"class":"scores teaching-score"})
  uni_research_score = score_soup.findAll("td", {"class":"scores research-score"})
  uni_citations_score = score_soup.findAll("td", {"class":"scores citations-score"})
  uni_industry_income_score = score_soup.findAll("td", {"class":"scores industry_income-score"})
  uni_international_outlook_score = score_soup.findAll("td", {"class":"scores international_outlook-score"})

  # Đóng trình duyệt
  web_driver_score.close()

  rank, names, countries, number_students, student_staff_ratio, intl_students, female_male_ratio, web_address = [], [], [], [], [], [], [], []

  overall_score, teaching_score, research_score, citations_score, industry_income_score, international_outlook_score = [], [], [], [], [], []

  for i in range(len(uni_name)):
      names.append(uni_name[i].text)
      rank.append(uni_stats_rank[i].text)
      countries.append(uni_location[i].text)
      number_students.append(uni_stats_number_students[i].text)
      student_staff_ratio.append(uni_stats_students_per_staff[i].text)
      intl_students.append(uni_stats_international_students[i].text)
      female_male_ratio.append(uni_stats_female_male_ratio[i].text[0:2])
      overall_score.append(uni_overall_score[i].text)
      teaching_score.append(uni_teaching_score[i].text)
      research_score.append(uni_research_score[i].text)
      citations_score.append(uni_citations_score[i].text)
      industry_income_score.append(uni_industry_income_score[i].text)
      international_outlook_score.append(uni_international_outlook_score[i].text)

  df = pd.DataFrame({
      'rank': rank,
      'name': names,
      'country': countries,
      'number_of_students': number_students,
      'student_per_staff': student_staff_ratio,
      'international_students': intl_students,
      'famale_male_ratio': female_male_ratio,
      'overall_score': overall_score,
      'teaching_score': teaching_score,
      'research_score': research_score,
      'citations_score': citations_score,
      'industry_income_score': industry_income_score,
      'international_outlook_score': international_outlook_score
  })

  # loại bỏ các hàng có cột rank là 'Reporter'
  df = df[df['rank'] != 'Reporter']
  # loại bỏ kí tự '%' trong cột 'International Students'
  df['international_students'] = df['international_students'].str.replace(pat='%', repl='')
  # loại bỏ kí tự `=` trong cột 'Rank'
  df['rank'] = df['rank'].str.replace(pat='=', repl='')
  # loại bỏ kí tự `-` và những kí tự trước đó của cột overall score
  df['overall_score'] = df['overall_score'].str.replace(
      pat='.*\–', repl='', regex=True)
  # loại bỏ kí tự `-` và những kí tự sau đó của cột 'Rank' và loại bỏ kí tự `+`
  df['rank'] = df['rank'].str.replace(
      pat='\–\d*|\+', repl='', regex=True)
  # bỏ dấu `,` trong cột 'Number of Students'
  df['number_of_students'] = df['number_of_students'].str.replace(pat=',', repl='')
  # thay thế giá trị `n/a` trong mọi cột thành NaN
  df = df.replace('n/a*', np.nan, regex=True)
  
  # xuất dữ liệu ra file csv
  df.to_csv(f'src/data/world_university_ranking_{year}.csv', index=False)

  year += 1

