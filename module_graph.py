import matplotlib.pyplot as plt
import numpy as np

def graphmaker(male_scores, female_scores, year, subject):

  x_values = np.arange(1, len(male_scores) + 1)

  plt.plot(x_values, male_scores, label='남자', marker='o')  
  plt.plot(x_values, female_scores, label='여자', marker='x')     
  

  
  plt.title(f'{year}학년도 수능 {subject}과목분포')  

  
  plt.xlabel('점수')   

  
  plt.legend()  

  
  plt.show()



