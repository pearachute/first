import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1653")

soup=BeautifulSoup(html, "lxml")
