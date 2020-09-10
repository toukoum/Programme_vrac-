# pendu.py
from tkinter import *
from getpass import getpass 
from random import *

fen = Tk()
fen.config(bg="#D1FEFF")
fen.title('_LE JEU DU PENDU_')
fen.minsize(400, 400)
# fen.configure(bg='#9DE6E8')

screen_x = int(fen.winfo_screenwidth())
screen_y = int(fen.winfo_screenwidth())
window_x = 600
window_y = 700
posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
fen.geometry(geo)

lbl_titre = Label(fen, text = 'LE JEU DU PENDU',bg='#D1FEFF', anchor = 'n',  font = ('Purisa', 25, 'underline'))
lbl_titre.grid(row=0, column = 0)

canvas = Canvas(fen, bg = '#9DE6E8', width = 598, height = 500)#550
canvas.grid(row= 1, column = 0) 


liste_capital = ["TIRANA", "BERLIN", "RIGA","VIENNE","BRUXELLES","MINSK",
"SARAJEVO","SOFIA","NICOSIE","ZAGREB","COPENHAGUE","MADRID","TALLIN",
"HELSINKI","PARIS","ATHENES","DUBLIN", "VADUZ", "ROME", "CHISINEAU", "VILNIUS",
"LUXEMBOURG","MONACO","SKOPJE","AMSTERDAM","LISBONNE","LONDRES","PRAGUE","BUCAREST",
"BUDAPEST", "OSLO", "RIGA","BRATISLAVA","PODGORICA","VARSOVIE","MOSCOU", "BELGRADE",
"LJUBJANA","KIEV","VATICAN","BERNE","STOCKHOLM","LA VALETTE", "RAPHAEL"]


# """""""""""""
def init ():
    global end, mot_en_progrès, secret, compteur, canvas
    secret=(choice(liste_capital))
    mot_en_progrès = list('*'*len(secret))
    stars = "".join(mot_en_progrès)
    the_mot["text"]= stars
    for Boutton in btns:
        Boutton['state']= NORMAL
    compteur=0
    if compteur == 0:
        annonce['text']=0 
    end = True
    canvas.delete(ALL)
    canvas.create_window(420, 420, window = the_mot)
    canvas.create_window(500, 480, window = nouvelle_partie)
    canvas.create_window(500, 50, window = annonce)
    canvas.configure(bg='#9DE6E8')
    the_mot.configure(bg='#9DE6E8')
    nouvelle_partie.configure(bg='#9DE6E8')
    annonce.configure(bg='#9DE6E8')        
    

def score(lettre):
    global compteur, end, dessine
    if lettre not in secret:
        compteur+=1
        canvas.create_line(50, 480, 150, 480, fill ="black", width = 8)
        if compteur == 2:
            canvas.create_line(100, 480, 100, 100, fill ="black", width = 8)
        elif compteur == 3:
            canvas.create_line(100, 100, 280, 100, fill ="black", width = 8)
        elif compteur == 4:
            canvas.create_line(100, 150, 150, 100, fill ="black", width = 8)
        elif compteur == 5:
            canvas.create_line(280, 100, 280, 130, fill ="black", width = 8)
        elif compteur == 6:
            canvas.create_oval(260, 130, 300, 180, width="5")
        elif compteur ==7:
            canvas.create_line(280, 180, 280, 270, fill ="black", width = 6)
            canvas.create_line(230, 240, 280, 200, fill ="black", width = 6)
            canvas.create_line(280, 200, 320, 240, fill ="black", width = 6)
        elif compteur ==8:
            canvas.create_line(230, 330, 280, 270, fill ="black", width = 6)
            canvas.create_line(280, 270, 330, 330, fill ="black", width = 6)
        if compteur>=limite:
            annonce['text']="PERDU !"
            end = False
            the_mot.configure(text=secret)
            canvas.configure(bg = 'red')
            the_mot.configure(bg='red')
            nouvelle_partie.configure(bg='red')
            annonce.configure(bg='red')
        else:
            annonce['text']=compteur
    elif mot_en_progrès == list(secret):
        annonce['text']="GAGNÉ !"
        end = False
        canvas.configure(bg ='green')
        the_mot.configure(bg='green')
        nouvelle_partie.configure(bg='green')
        annonce.configure(bg='green')
  
  
def maj_lettre(lettre, secret, mot_en_progrès):
    n=len(secret)
    for i in range(n):
        if secret [i]==lettre:
            mot_en_progrès[i]=lettre
            


def choisir_lettre(event):
    if end == False:
        return
    mon_boutton = event.widget
    lettre= mon_boutton["text"]
    mon_boutton["state"]=DISABLED
    maj_lettre(lettre, secret, mot_en_progrès)
    the_mot["text"]="".join(mot_en_progrès) 
    score(lettre)


the_mot = Label(fen, font ="Times 20 bold", bg = '#9DE6E8' )
canvas.create_window(420, 420, window = the_mot)
nouvelle_partie = Button(canvas, text = 'Nouveau', command = init)
canvas.create_window(500, 480, window = nouvelle_partie)
annonce = Label(canvas, width = 10, text = 0, font ="Times 20 bold", bg = '#9DE6E8')
canvas.create_window(500, 50, window = annonce)

end = True 
compteur=0
limite = 8
btns = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

clavier_1 = Frame(fen, bg='#D1FEFF')
clavier_1.grid(row=2, column=0, )

for x in range(2):
    for y in range(10):
        Boutton_1 = Button(clavier_1, text = alpha[10* x+y],bg='white', relief = FLAT, font ='TIMES 15') 
        Boutton_1.grid(row= x, column=y, pady = 5)
        Boutton_1.bind('<Button-1>', choisir_lettre)
        btns.append(Boutton_1)

for y in range(6):
    Boutton_1 = Button(clavier_1, text = alpha[20+y],bg='white', relief = FLAT, font ='TIMES 15') 
    Boutton_1.grid(row=x+1, column = y+2)
    Boutton_1.bind('<Button-1>', choisir_lettre)
    btns.append(Boutton_1)

boutton_quit = Button(clavier_1, text = "QUITER",bg = '#D1FEFF', command = quit)
boutton_quit.grid(row=x+1, column = y+4)

init()
ouverture = getpass()

fen.mainloop()



