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
            G[u][v]['weight'] = random.randint(1, 10)
    return G

# noeuds -> nx
# lignes -> plt
def afficher_graphe(G, option_poids):
    couleurs = ["#CCFF66" if node == "A" else "#FFCC99" for node in G.nodes()]

    pos = nx.spring_layout(G, seed = 42)
    
    nx.draw(G, with_labels=True, node_color=couleurs, edge_color="gray")
    if option_poids:
        poids_vertice = {}
        for u, v, data in G.edges(data = True):
            poids_vertice[(u, v)] = data['weight']
        nx.draw_networkx_edge_labels(G, pos, edge_labels=poids_vertice)
    
    plt.show()


def parcours_profondeur(G):
    
if __name__ == "__main__":
    G = generer_graphe(random.randint(5,10), 0.3, False)
    afficher_graphe(G, False)
