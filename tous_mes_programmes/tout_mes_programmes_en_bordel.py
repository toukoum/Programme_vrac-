import statistics
import random 
import shuffle


#popcorn et age pour le ciné
age = int(input("Quel est votre age ?"))

if age>=18:
	prix_total=12
else:
    prix_total = 7	

request_pop_corn= input("souhaitez vous du pop corn ?(oui;Oui;OUI;non)") 

if request_pop_corn==("oui"):
   prix_total+=5 

print ('prix_total')


#test liste 
online_players=['raph','coco','laeti','paul']
print (online_players)
print(online_players[0])
print(online_players[len(online_players)-1])
	


#insta age verification
age_de_lutilisateur= int(input("Quel est votre age :"))
if age_de_lutilisateur<13:
	print("interdiction")
elif age_de_lutilisateur < 15:	
	print("autorisation")
else:
    print('libre') 	


#total kilometre < a 45 (marche pas)
total_kilometre=0

while total_kilometre<45:
	nombre_de_kilometre_parcouru= int(input("entrez votre nombre de kilometre aujourd'hui:"))
	total_kilometre = nombre_de_kilometre_parcouru+total_kilometre                              

print("felicitation !!")


#BASTIEN 
prenom = input("quel est votre prénom?")
if prenom == ('bastien'):
	print("bonjour bastien")	



#TABLE DE MULTIPLICATION
for result in range (1,10):
	print ("table de multiplication de :", result)
	for j in range (1,11):
		print (result*j)



#multiple de 25
x = int(input("donner la valeur de x :"))
y =25
print(x*y)


#ville et code postale
ville = input("donner le nom de votre ville :")
code_postal = input("donner le code postal de votre ville :")
print ("le code postal de", ville,"est", code_postal)



#if elif difference
x=int(input("donner un nombre :"))
if x>100:
	print("x est grand")
elif x>200:
	print ("x est très grand")
else:
	print ("x est petit")


#voulez vous continuez ?
rep = ("oui")
while rep ==("oui"):
	rep=input("voulez vous continuez ?")



#donner tt les h d'une journée
for i in range (0,25):
	for j in range (0,61):
		print(i, "heure", j, "min")



#plus grande valeur 
first= int(input("Donnez le nombre x :"))
second= int(input("Donnez le nombre n :"))

def max(x, n):
	if x>n:
		return x
	else:
		return n

print("la plus grande valeur est",max(first, second))



def get_vowels_number (word):
	nb_vowels=0

	for letter in word :
		if letter in["a", "e", "i", "o", "u", 'y']:
			nb_vowels+=1
	
	return nb_vowels

word=input("donnez un mot :")
compteur=get_vowels_number(word)
print("il y a", compteur,'voyelles dans le mot', word)
if compteur==0:
	print("il n'y a aucune voyelle dans le mot", word)


#année fin/debut 
def next_year():
	global year 
	print("fin de l'année", year)
	year+=1
	print("début de l'année", year)

year=2020
for next_year in range (4):




#dire cb de voyelles ya dans un mot 
def get_vowels_number (word):
	nb_vowels=0

	for letter in word :
		if letter in["a", "e", "i", "o", "u", 'y']:
			nb_vowels+=1
	
	return nb_vowels

word=input("donnez un mot :")
compteur=get_vowels_number(word)
print("il y a", compteur,'voyelles dans le mot', word)
if compteur==0:
	print("il n'y a aucune voyelle dans le mot", word)



#definir moyenne (PAS FINI !!)
while rep == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", 
"14", "15", "16", "17", "18", "19", "20"]:
	rep=int(input("entrez un nombre :"))
	if 

def moyenne (rep):
	return((rep)/compteur)
	
print(moyenne(rep))


	 
#activité du livre de maths le grossiste
from math import *
x=("prix total")
carte= input("Avez vous la carte de fidélité ?(o/n)")
nb_kilo=int(input('combien de kilo voulez vous ?'))
if nb_kilo<=100:
	x=nb_kilo*1.40
elif nb_kilo<=300:
	x=100*1.40+(nb_kilo-100)*1.10
else:
	if carte==("o") or carte==("O"):
		x=100*1.40+(nb_kilo-100)*1.10
		x*=0.9
	else:
		x=100*1.40+(nb_kilo-100)*1.10
print("Vous devez payer :", x, "euros")

#convertisseur pas fini 
unité=print(" km3, hm3, dam3, m3, dm3, cm3, mm3, kL, hL, daL, L, dL, cL, mL ")
x=input('Parmi les unités ci-dessus, quelle est la valeur que vous voulez convertir :')
y=input('Dans quelle unité voulez vous la convertir :')
z=int(input('Entrez la valeur a convertir :'))

if x==('km3') and y==('hm3'):
	z*=10

print(z, y)


#guichet automatique 
print("Bonjour, veuillez selectionner la distance de votre voyage, votre âge, et votre heure de départ ci-dessous")
distance=int(input("A quelle distance voulez vous voyager :"))
âge=int(input("Quelle est votre âge :"))
heure=int(input("Quelle est votre heure de départ :"))
tarif_total=0

if distance<10:
	tarif_total+=1.20
elif distance<25:
	tarif_total+=2
else:
	tarif_total+=2.50


if âge<10:
	tarif_total*=0.75
elif âge>65:
	tarif_total*=0.10


if heure <7:
	tarif_total*=0.95
elif heure<10:
	tarif_total*=1.10
elif heure<16 and heure<19:
	tarif_total*=1.10
elif heure >19:
	tarif_total*=0.95

print("Vous devez payer :", tarif_total, "euros, merci !")

#4*4 accidenté
x=60
y=0
z=0.005
while x>0:
	y+=1
	x-=0.1
	x-=z
	if y%4==0:
		z*=2
	print(y, "km", x, "L de carburant")

#nb premier ou ap 
from math import*
def nb_premier(x):
	division = 2
	while division<=sqrt(x):
		if nb_premier%2==0:
			return False
		division+=1
	return True 

def liste_nb_premier(debut, fin):
	liste=[]
	for nombre in range(debut,fin+1,1):
		if nb_premier(nombre):
			liste.append(nombre)
	return liste 

print(len(liste_nb_premier(2,5000)))
print(len(liste_nb_premier(5001,10000))) 




#défis manuel fonction sans parametre et découverte de turtle 
import turtle 

def Maison():
	turtle.left(90)
	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)
	turtle.left(90)
	
turtle.reset()
turtle.up()
turtle.goto(0, 0)
turtle.down()
turtle.speed(1)


for n in range(4):
	Maison()
	turtle.rt(90)
	turtle.forward(20.71)
	turtle.lt(90)
	turtle.forward(20.71)
	turtle.rt(90)
	#turtle.rt(90)

turtle.exitonclick()


x = int(input('Entrez un nombre entier :'))
print('Les diviseurs de', x,'sont :')
for n in range (1,x+1):
    if x%n==0:
        print(n) 


#le jeu du juste prix
from random import *

x=randint(0,100)
n=0
compteur=0
while n!=x:
    n=int(input("Entrez une valeur :"))
    compteur+=1
    if compteur>=7:
        print(' TA PERDU ')
        break 
    if n<x:
        print('C plus')
    if n>x:
        print('C moins')
    if n==x:
        print('BIEN JOUE')
   
# test liste remove


emails= ['raph@gir', 'isa@gir', 'steph@gir']
blacklist=["isa@gir"]


for email in emails:
	if email in blacklist:
		print ("envoie {} impossible !".format(email))
		emails.remove(email)
		continue 

print ('Email envoyé à :', emails)


    