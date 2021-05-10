import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1653")

soup=BeautifulSoup(html, "lxml")

tourist_table = soup.find_all('table', {'id':'t_Table_165301'})
tourist_table_tbody = tourist_table[0].find_all('tbody')
tourist_table_tbody_row = tourist_table_tbody[0].find_all('tr')
tourist_table_tbody_row.remove(tourist_table_tbody_row[1])
x_axes=[]
d=[]
td = tourist_table_tbody_row[0].find_all('td')

for content in td:
    d.append(content.get_text())

for i in d:
    i_1=i.replace(',','')
    i_1=int(i_1)
    x_axes.append(i_1)
print(x_axes)
year = []

for i in range(2011,2021):
    year.append(i)

plt.rc('font', family='Malgun Gothic')
fig, ax1 = plt.subplots()
ax1.set_title('방한 외래관광객')
ax1.plot(year, x_axes, '-o',color="red")
plt.bar(year,x_axes,color='gray')
plt.show()