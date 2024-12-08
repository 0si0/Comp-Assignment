import pandas as pd

data = None
subject_category = set()

def choose_file_path(year):
    global data, subject_category
    year = int(year)-1
    file_path = f'{year}1231.csv'
    data = pd.read_csv(file_path, encoding='cp949')

    subject_category.clear()
    for i in data["유형"]:
        subject_category.add(i)

def make_data(subject):
    filtered_data = data[data['유형'] == subject]

    max_score = filtered_data['표준점수'].tolist()
    male_count = filtered_data['남자'].tolist()
    female_count = filtered_data['여자'].tolist()

    return male_count, female_count, max_score
