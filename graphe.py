import dash
from dash import html, dcc, Output, Input, State
import dash_cytoscape as cyto
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import string
import heapq

# genere un graphe aleatoire
def generer_graphe(nb_noeuds, vertice_proba, option_poids):
    G = nx.gnp_random_graph(nb_noeuds, vertice_proba)
    
    # ajout d'attributs parent, visité et distance
    nx.set_node_attributes(G, False, "marque")  
    nx.set_node_attributes(G, None, "parent") 
    nx.set_node_attributes(G, 0, "distance") 
    
    
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

# PARCOURS EN PROFONDEUR
# le sommet de départ sera toujours 'A' et si le graphe n'est pas connexe on y va en ordre alphabetique
def parcours_profondeur(G):
    for noeud in G.nodes:       
        if G.nodes[noeud]['marque'] == False:
            visiter_profondeur(G, noeud)
   
def visiter_profondeur(G, noeud):
    G.nodes[noeud]['marque'] = True
    print(noeud)
    for voisin in G.neighbors(noeud):
        if G.nodes[voisin]['marque'] == False:
            G.nodes[voisin]['parent'] = noeud
            G.nodes[voisin]['distance'] = G.nodes[noeud]['distance'] + 1
            visiter_profondeur(G, voisin)
    
def parcours_largeur(G): 
     for noeud in G.nodes: 
        if G.nodes[noeud]['marque'] == False:
            visiter_largeur(G, noeud)
    
def visiter_largeur(G, noeud):
    G.nodes[noeud]['marque'] = True
    print(noeud)
    file = []
    heapq.heappush(file, noeud)
    while file:
        noeud = heapq.heappop(file)
        for voisin in G.neighbors(noeud):
            if G.nodes[voisin]['marque'] == False:
                G.nodes[voisin]['parent'] = noeud
                G.nodes[voisin]['distance'] = G.nodes[noeud]['distance'] + 1
                G.nodes[voisin]['marque'] = True
                heapq.heappush(file, voisin)
                print(voisin)
            
        
    
if __name__ == "__main__":
    G = generer_graphe(random.randint(5,10), 0.3, False)
    afficher_graphe(G, False)
    parcours_largeur(G)

# pour les noeuds interactifs
# si on clic et la comparaison de parcours ok 
#   -> noeud change de couleur
#   -> you cant click on it anymore
#
# si on clic et il y a une erreur dans le parcours
#   -> node becomes red and fades back to orange
#