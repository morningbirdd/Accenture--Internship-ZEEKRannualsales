import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sales_2022 = 19011 
sales_2023 = 42633 
change = 224.25 

fig = plt.figure(figsize=(8, 6))

ax1 = fig.add_subplot(111)
ax1.set_title('极氪汽车上半年零售销量')
ax1.set_xlabel('年份')
ax1.set_ylabel('销量（辆）')
ax1.set_xticks([1, 2])
ax1.set_xticklabels(['2022', '2023'])
ax1.bar([1, 2], [sales_2022, sales_2023], color=['pink', 'skyblue'], width=0.4)
ax1.text(0.9, sales_2022 + 1000, f'{sales_2022}')
ax1.text(1.9, sales_2023 + 1000, f'{sales_2023}')
ax2 = ax1.twinx()
ax2.set_ylabel('同比变化（%）')
ax2.plot([1, 2], [0, change], color='green', linestyle='--', marker='o')
ax2.text(1.05, 0, '0%')
ax2.text(2.05, change, f'{change}%')

plt.show()
