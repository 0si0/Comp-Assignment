import pandas as pd

def get_gender_score(file_path, subject):

    data = pd.read_csv(file_path, encoding='cp949')
    
    filtered_data = data[(data['유형'] == subject)]
    subjects = data['유형'].drop_duplicates().tolist()
    male_count = filtered_data['남자'].tolist()
    female_count = filtered_data['여자'].tolist()
    
    return subjects, male_count, female_count


file_path = '20231231.csv'

male_count, female_count = get_gender_score(file_path, '국어')

