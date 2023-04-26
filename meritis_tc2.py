"""

Une pléthore de chronobots
Le nombre d'anomalies à corriger semble immense et pourtant le budget de la Brigade des Anomalies Chronologiques n'est pas infini. Votre responsable vous demande le nombre de chronobots pour effectuer l'ensemble des missions à couvrir.

Pour chacune des n missions, vous connaissez sa date de début di et sa date de fin fi (toutes deux en jours).

Le protocole des chronobots est simple :

le chronobot est envoyé dans le passé une unique fois, au début de sa première mission;
ensuite, le chronobot ne peut ensuite se déplacer que vers le futur, allant instantanément de la fin de sa mission précédente au début de sa nouvelle mission pour commencer cette dernière immédiatement;
lorsque le chronobot a terminé sa dernière mission, il sera recyclé où il a fini.
Combien de chronobots au minimun sont nécessaires pour effectuer les n missions ?

En entrée un fichier organisé comme suit

sur une première ligne vous trouverez un entier n
sur chacune des n lignes suivantes, vous trouverez à la ième ligne séparés par des espaces di, et fi
En réponse

le nombre minimal de chronobots nécessaires

https://github.com/chaimleib/intervaltree
"""
from collections import deque
from random import choice
from time import perf_counter
from typing import List


def recherche_dichotomique(mission: tuple, missions: List[tuple]) -> int:
    a = 0
    b = len(missions) - 1
    m = (a + b) // 2
    while a <= b:
        if missions[m][0] >= mission[1]:
            # m ok
            b = m - 1
        else:
            # m ko
            a = m + 1
        m = (a + b) // 2
    return a if a < len(missions) else None


if __name__ == "__main__":
    n = int(input())

    tic = perf_counter()

    missions: List[tuple] = [tuple(map(int, input().split())) for _ in range(n)]
    missions = sorted(missions, key=lambda m: m[0])
    print(f'sort time = {round((perf_counter() - tic) * 1000, 2)} ms')

    """Zorg — Aujourd’hui à 00:28
    faut pas trier les mission par date de début ?
    b0n5a1 — Aujourd’hui à 00:28
    au boulot y'en a un il avait une sorte d'écharde dans l'oeil (en Suisse)...il est allé chez un toubib suisse en urgence...et à la pharmacie un pauvre collyre et je sais plus quoi il en avait pour plus de 150 balles (heureusement c'est couvert par l'assurance privée ces conneries aussi...tu peux te faire soigner des deux côtés de la frontière pour une urgence)
    Zorg — Aujourd’hui à 00:28
    bah représente toi ça comme des segment sur un axe"""

    """
        [ ] - Tu prends la mission la plus tôt non encore prise, ensuite tu cherches la première possible qui démarre après la fin de ta courante (cette recherche se fait en dicho au lieu de O(n)) etc 
        [ ] - Tu réiteres ça avec d'autres bots"""
    chronobots: int = 0

    while missions:
        m = missions.pop(0)
        # print(f'chronobot {chronobots} start -> {m}')
        # history = set()
        missions_count: int = 0
        j = recherche_dichotomique(m, missions)
        while j:
            # print(f'next -> {missions[j]}')
            m = missions.pop(j)
            missions_count += 1
            j = recherche_dichotomique(m, missions)

        chronobots += 1
        # print(f'chronobot {chronobots} completed {missions_count} missions! ({len(missions)} remaining missions)')
        # print(f'{chronobots} - {len(missions)}')

    print(f'result = {chronobots - 1}')
    print(f'elapsed time = {round((perf_counter() - tic) * 1000, 2)} ms')
