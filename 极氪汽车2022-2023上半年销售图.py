import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

years = [ '2021', '2022', '2023']
sales = [7.19, 5.47, 4.26]
font = FontProperties(fname="C:\Windows\Fonts\SimHei.ttf") 
plt.bar(years, sales)
plt.xlabel('年份', fontproperties=font)
plt.ylabel('销量（单位：万辆）', fontproperties=font)
plt.title('极氪汽车2021-2023年上半年零售销量', fontproperties=font)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()