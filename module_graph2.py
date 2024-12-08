import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())

def graphmaker(male_scores, female_scores, year, subject, max_scores):
    x_values = np.arange(max_scores[0] - len(male_scores) + 1, max_scores[0] + 1)

    plt.bar(x_values - 0.2, male_scores, width=0.4, label='남자', align='center')
    plt.bar(x_values + 0.2, female_scores, width=0.4, label='여자', align='center')

    plt.title(f'{year}학년도 수능 {subject} 과목분포')
    
    plt.xlabel('표준점수')
    plt.ylabel('응시자 수')
    plt.xlim(max_scores[0] - len(male_scores), max_scores[0] + 1)
    
    plt.legend()
    plt.show()
