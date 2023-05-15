import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/world_university_ranking_2023.csv')

# lọc lấy những cột có giá trị là số
df = df.select_dtypes(include=['int64', 'float64'])

# tạo heatmap
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Blues')

# update layout
plt.tight_layout()

plt.show()

