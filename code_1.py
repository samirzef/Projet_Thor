 # Implémente l'algorithme de Johnson pour résoudre le problème F2||Cmax.

def johnson_algorithm(tasks):
    
    # tasks: Liste de tuples [(P1, P2), ...] où P1 est le temps sur M1 et P2 est le temps sur M2.
     
    # Séparer les tâches en deux groupes selon P1 et P2

    S1 = []  # Tâches pour M1 (P1 <= P2)
    S2 = []  # Tâches pour M2 (P1 > P2)
    for i, (P1, P2) in enumerate(tasks):
        if P1 <= P2:
            S1.append((i + 1, P1, P2))  # Inclure l'index de la tâche pour la traçabilité
        else:
            S2.append((i + 1, P1, P2))

    # Étape 2 : Trier S1 par P1 croissant, et S2 par P2 décroissant
    S1.sort(key=lambda x: x[1])  # Trier par P1
    S2.sort(key=lambda x: x[2], reverse=True)  # Trier par P2 décroissant

    # Construire la séquence optimale
    sequence = [task[0] for task in S1] + [task[0] for task in S2]

    # Calculer le Cmax pour la séquence

    current_time_M1 = 0    # Initialisation des temps
    current_time_M2 = 0
    for task_index in sequence:
        P1, P2 = tasks[task_index - 1]  # Récupérer les temps pour la tâche
        current_time_M1 += P1
        current_time_M2 = max(current_time_M1, current_time_M2) + P2

    Cmax = current_time_M2

    return sequence, Cmax


# Exemple 
tasks = [(3, 6), (2, 8), (7, 4), (5, 3)]  # Ti=(P1, P2)   [T1,T2,T3,T4]
sequence, Cmax = johnson_algorithm(tasks)

print("L'ordre optimal est :",sequence)
print("Cmax = ",Cmax)