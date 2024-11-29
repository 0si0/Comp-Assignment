import module_readscore as mr
import module_graph as mg




print("연도를 선택하세요.  2024")
user_year = input()

while user_year != "2024":
  print("준비되지 않은 연도입니다.")
  user_year = input()

for i in mr.subject_category:
  print(i)
print("과목을 선택하세요.")
user_subject = input()
while user_subject not in mr.subject_category:
  print("준비되지 않은 과목입니다.")
  user_subject = input()


male_count, female_count, max_score = mr.make_data(user_subject)
mg.graphmaker(male_count, female_count, user_year, user_subject, max_score[0])









