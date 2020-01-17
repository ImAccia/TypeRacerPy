import time
import bs4
import random
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import threading
import pyautogui
import os
import plotly
import plotly.graph_objects as go

def mytimer():
    print("\n\nTempo scaduto\n")
    pyautogui.press('enter')
    
my_timer = threading.Timer(10, mytimer) 

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

notizia = random.randint(0,10)
i = 0
testo = ""
for news in news_list:
    if i == notizia:
        testo = news.title.text
    i = i + 1

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
my_timer.start() 
print("Tempo iniziato\n")
print(testo+"\n")


testoGuessed = input()

testoLista = testo.split(" ")
testoGuessedLista = testoGuessed.split(" ")

x = len(testoLista)
y = len(testoGuessedLista)
a = 0
for j in range(0,y):
    if testoLista[j] == testoGuessedLista[j]:
        a = a+1
if a == 0:
    print("Hai indovinato 0 parole")
    quit()
    
print("Hai indovinato "+str(a)+" parole")


path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
path1 = path+"\\record.txt"



bars1 = []
bars2 = []
nomi=[]
creazione = open(path1, 'a')
creazione.close()
dati = open(path1, 'r+')
for line in dati:
    nomi.append(line.split(';')[0])
    bars1.append(line.split(';')[1])
    bars2.append(line.split(';')[2].replace("\n",""))



nome = input("Con che nome desideri salvare il tuo record? ")

while nome in nomi:
    print("Il nome è già presente, cambiare nome\n")
    nome = input()

bars1 = []
bars2 = []
nomi=[]


scrittura = open(path1, 'a+')
scrittura.write(str(nome)+";"+str(x)+";"+str(a)+"\n")
scrittura.close()

dati = open(path1, 'r+')
for line in dati:
    nomi.append(line.split(';')[0])
    bars1.append(line.split(';')[1])
    bars2.append(line.split(';')[2].replace("\n",""))




fig = go.Figure()
fig.add_trace(go.Bar(
    x=nomi,
    y=bars1,
    name='Parole Totali',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=nomi,
    y=bars2,
    name='Parole Indovinate',
    marker_color='lightsalmon'
))



# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)

plotly.offline.plot(fig, filename=path+'graph.html')
