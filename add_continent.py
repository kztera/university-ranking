import pandas as pd

def add_column_continent(df):
  asia = ['China', 'India', 'Indonesia', 'Japan', 'South Korea', 'Malaysia', 'Philippines', 'Thailand', 'Vietnam', 'Turkey', 'Hong Kong', 'Sri Lanka', 'Lebanon', 'Singapore', 'United Arab Emirates', 'Oman', 'Taiwan', 'Iraq', 'Bangladesh', 'Iran', 'Macao', 'Nepal', 'Pakistan', 'Brunei Darussalam', 'Jordan', 'Israel', 'Kazakhstan', 'Georgia', 'Northern Cyprus', 'Kuwait', 'Palestine', 'Qatar', 'Saudi Arabia']

  arfica = ['Egypt', 'Morocco', 'Nigeria', 'South Africa', 'Tunisia', 'Zimbabwe', 'Zambia', 'Ghana', 'Kenya', 'Algeria', 'Ethiopia', 'Uganda', 'Namibia', 'Mozambique', 'Tanzania', 'Botswana', 'Mauritius']

  north_america = ['Canada', 'United States', 'Cuba', 'Costa Rica', 'Jamaica', 'Puerto Rico']

  south_america = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Mexico', 'Peru', 'Venezuela']

  europe = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Iceland', 'Russian Federation', 'Belarus', 'Montenegro', 'Greece', 'Azerbaijan']

  australia = ['Australia', 'New Zealand', 'Fiji']

  df['continent'] = ""

  for index, row in df.iterrows():
    if row['country'] in asia:
      df.at[index, 'continent'] = 'Asia'
    elif row['country'] in arfica:
      df.at[index, 'continent'] = 'Africa'
    elif row['country'] in north_america:
      df.at[index, 'continent'] = 'North America'
    elif row['country'] in south_america:
      df.at[index, 'continent'] = 'South America'
    elif row['country'] in europe:
      df.at[index, 'continent'] = 'Europe'
    elif row['country'] in australia:
      df.at[index, 'continent'] = 'Australia'
