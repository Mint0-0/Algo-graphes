import networkx as nx
import matplotlib.pyplot as plt
import random
import string

# genere un graphe aleatoire
def generer_graphe(nb_noeuds, vertice_proba, option_poids):
    G = nx.gnp_random_graph(nb_noeuds, vertice_proba)
    # lettre pour les noeuds
    mapping = {i: string.ascii_uppercase[i] for i in range(nb_noeuds)}
    G = nx.relabel_nodes(G, mapping)
    
    # si on veut des poids aux vertices
    if option_poids:
        for u, v  in G.edges():
            G[u][v]['weight'] = random.randint(1, 15)
    return G

# noeuds -> nx
# lignes -> plt
def afficher_graphe(G, poids=False):
    nx.draw(G, with_labels=True, node_color="pink", edge_color="gray")
    plt.show()

if __name__ == "__main__":
    G = generer_graphe(random.randint(10,15), 0.3, True)
    afficher_graphe(G)
