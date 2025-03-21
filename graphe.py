import networkx as nx
import matplotlib.pyplot as plt
import random

# genere un graphe aleatoire
def generer_graphe(nb_noeuds, vertice_proba, option_poids):
    G = nx.gnp_random_graph(nb_noeuds, vertice_proba)
    # si on veit des poids aux vertices
#    if option_poids:
# 	for() in G.edges():
#	    G[][]['weigth'] = random.randint(1, 15)
    return G

# noeuds -> nx
# lignes -> plt
def afficher_graphe(G, poids=False):
    nx.draw(G, with_labels=True, node_color="pink", edge_color="gray")
    plt.show()

if __name__ == "__main__":
    G = generer_graphe(random.randint(10,15), 0.3, False)
    afficher_graphe(G)
