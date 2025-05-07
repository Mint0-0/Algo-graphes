import dash
from dash import html, dcc, Output, Input, State
import dash_cytoscape as cyto
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import string

app = dash.Dash(__name__)
cyto.load_extra_layouts()

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


def conversion_nx_cytoscape(G, option_poids):
    elements = []
    
    # conversion des sommets
    for node in G.nodes():
        donnee_sommet = {
            'data': {'id': node, 'label': node}
        }
        elements.append(donnee_sommet)
    
    # conversion des arêtes
    for u, v in G.edges():
        donnee_arete = {
            'source': u,
            'target': v
        }
        elements.append({'data': donnee_arete})
        
    print(elements)
    return elements

app.layout = html.Div([
    html.H1("Graphe aléatoire"),
html.Div([
        html.Button("Générer le graphe", id='generate-btn'),
    ], style={'margin-bottom': '20px'}),
    
     cyto.Cytoscape(
        id='cytoscape-graph',
        layout={'name': 'cose'},
        style={'width': '100%', 'height': '500px'},
        elements=[]
    ) 
    ])

@app.callback(
    Output('cytoscape-graph', 'elements'),
    Input('generate-btn', 'n_clicks'),
)

def generer_graphe_dash(n_clicks):
    nb_noeuds = random.randint(5, 10)
    proba = 0.3
    option_poids = False

    G = generer_graphe(nb_noeuds, proba, option_poids)
    elements = conversion_nx_cytoscape(G, option_poids)
    return elements


def update_graph(n_clicks):
    if n_clicks is None:
        return []

    nb_noeuds = random.randint(5, 10)
    proba = 0.3
    option_poids = False  

    G = generer_graphe(nb_noeuds, proba, option_poids)
    elements = conversion_nx_cytoscape(G, option_poids)
    return elements

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
    
if __name__ == "__main__":
   # G = generer_graphe(random.randint(5,10), 0.3, False)
   # conversion_nx_cytoscape(G, False)
    app.run(debug=True)
    #afficher_graphe(G, False)
    #parcours_largeur(G)

# pour les noeuds interactifs
# si on clic et la comparaison de parcours ok 
#   -> noeud change de couleur
#   -> you cant click on it anymore
#
# si on clic et il y a une erreur dans le parcours
#   -> node becomes red and fades back to orange
#