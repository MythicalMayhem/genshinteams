from bs4 import BeautifulSoup
import webbrowser
import os


with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

alts = []
imgs = soup.findAll('img')
for img in imgs:
    alts.append(img['alt'])
alts = list(set(alts))
alts.remove('Electro')
alts.remove('Geo')
alts.remove('Anemo')
alts.remove('Cryo')
alts.remove('Pyro')

n = input('Choose a character : ')
parents = []

if n in alts :
    imgs = soup.findAll("img",alt=n)
    for img in imgs:
        parents.append(img.find_parent('div'))

with open('open.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n')
    for parent in parents:
        f.write(str(parent))
    f.write('</body></html>')
    f.close()   
    
filename = 'file:///'+os.getcwd()+'/' + 'open.html'
webbrowser.open_new_tab(filename)