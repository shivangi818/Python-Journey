lyrics=""" Oh God, one more Remix?

Ho dil dhadkaaye
(hey hey..)
Arey seeti bajaye
(hey hey..)
Haye dil dhadkaye, seeti bajaye
Beech sadak pe nakhre dikhaye
Saare, ho karke ishare
Ho ladki.. aan aan aan…
Ho ladki.. aan aan aan…

Oh ladki aankh marey
Aankh maare
Oh ladki aankh marey
Aankh maare
Oh ladki aankh marey

(hey hey…)

Jahaan jahaan jaaun
Mere peeche peeche aaye
Gali gali ke aashiq
Dono mera hona chaahe

Tang tang tang… wakao
Tang tang tang…

Haaye jahaan jahaan jaaye
Tere peeche peeche aaye
Hum toh hai deewane tere
Tera hona chaahe

Seeti bajaye
(hey hey hey)
Nakhre dikhaye
(hey hey hey)
Seeti bajaye nakhre dikhaye
Beech sadak mein haye naam mera pukare
Oh kar ke ishare
O ladka aan aan aan…
O ladka aan aan aan…
O ladka.. aankh maare
Oh ladki aankh maare
Aankh maare
Oh ladki aankh maare
Aankh marey

Tushar Kapoor ki awaaz mein
Ee ow aan aan aan…
Ee ow aan aan aan…
Ee ow aan aan aan…

Kumar Sanu ki aawaz mein

Oh ladki aankh maare
Aankh marey
Oh ladki aankh maare
Aankh marey
Oh ladki aankh maare

Aan aan aan…
O ladka.. aan aan aan…
O ladki.. aan aan aan…
O ladka.. aan aan aan…

Aan aan aan…
Aan aan aan…"""

L=lyrics.split()
print(L)


D={}
for i in L:
    if i in D:
        #false
        D[i]=D[i]+1
    else:
        D[i]=1

m=max(D.values())
for i in D:
    if D[i]==23:
        print(i)
      
print(len(D))

