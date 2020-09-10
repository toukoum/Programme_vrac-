
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(liste)):
    liste.append(liste[x])

def chiffrement(lettre, liste, clés):
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste [i]==lettre:
            return str(liste[i + clés])
    return '?'

message_chiffré = str()

message = input('Entrez votre message à coder :')
clés =  int(input('Entrez votre clé de chiffrement :'))
for lettre in message:
    message_chiffré += chiffrement(lettre, liste, clés)

print (message_chiffré)