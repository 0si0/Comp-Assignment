import pandas as pd

file_path = '20231231.csv'
data = pd.read_csv(file_path, encoding='cp949')

subject_category = set()
for i in data[""]:
  subject_category.add(i)

subject = input("과목: ")
filtered_data = data[data['유형'] == subject]

scores = filtered_data['표준점수'].tolist()
male_count = filtered_data['남자'].tolist()
female_count = filtered_data['여자'].tolist()

