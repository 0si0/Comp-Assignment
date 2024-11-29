import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import matplotlib.font_manager as fm


font_path = 'C:/Windows/Fonts/malgun.ttf'  

font_prop = fm.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())

def graphmaker(male_scores, female_scores, year, subject, max_score):

  x_values = np.arange(max_score - len(male_scores) + 1, max_score + 1)

  plt.plot(x_values, male_scores, label='남자')  
  plt.plot(x_values, female_scores, label='여자')     
  

  
  plt.title(f'{year}학년도 수능 {subject}과목분포')  

  
  plt.xlabel('표준점수')   
  plt.xlim(0, max_score)
  
  plt.legend()  

  
  plt.show()



