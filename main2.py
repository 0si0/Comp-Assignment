import module_readscore2 as mr
import module_graph2 as mg

available_years = ["2020", "2021", "2022", "2023"]
print("연도를 선택하세요. (2021, 2022, 2023, 2024)")
user_year = input()

while user_year not in available_years:
    print("준비되지 않은 연도입니다.")
    user_year = input()

mr.choose_file_path(user_year)  

for i in mr.subject_category:
    print(i)
print("과목을 선택하세요.")
user_subject = input()
while user_subject not in mr.subject_category:
    print("준비되지 않은 과목입니다.")
    user_subject = input()

male_count, female_count, max_score = mr.make_data(user_subject)
mg.graphmaker(male_count, female_count, user_year, user_subject, max_score)
