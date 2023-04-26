"""
Premier jour
Vous êtes en charge du déploiement des chronobots de la Brigade des Anomalies Chronologiques, des robots autonomes programmés pour corriger les anomalies de l’histoire.

Pour votre premier jour, vous voulez avoir le plus d'impact possible, et choisir de corriger l'anomalie qui rapporte le plus.

Pour chacune des n missions possibles, vous connaissez son revenu ri On vous fournit la liste des n missions possibles avec leur revenu ri, à vous de choisir laquelle effectuer.


En entrée un fichier organisé comme suit
sur une première ligne vous trouverez un entier n
sur chacune des n lignes suivantes, vous trouverez à la ième ligne ri

En réponse

l'id i de la mission que vous choisissez d'effectuer ( indexés à 1 )
"""
from typing import List

n = int(input())

incomes: List[int] = [int(input()) for _ in range(n)]

print(incomes.index(max(incomes)) + 1)

