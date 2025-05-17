import dash
from dash import html, dcc, Output, Input, State
import dash_cytoscape as cyto
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import string
from parcours import parcours_profondeur, parcours_largeur

app = dash.Dash(__name__, prevent_initial_callbacks='initial_duplicate')
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
            'data': {'id': node, 'label': node},
        }
        elements.append(donnee_sommet)
    
    # conversion des arêtes
    for u, v in G.edges():
        donnee_arete = {
            'source': u,
            'target': v
        }
        elements.append({'data': donnee_arete})
        
    return elements

app.layout = html.Div([
    html.H1("Graphe aléatoire"),
    html.Div([
        html.Button("Générer le graphe", id='generate-btn'),
        html.Button("Retour", id='retour'),
    ],
    style={'display': 'flex',
            'gap': '10px',  
            'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='parcours-option',
        options=[
            {'label': 'Parcours en profondeur', 'value': 'profondeur'},
            {'label': 'Parcours en largeur', 'value': 'largeur'}
                ],
        value='profondeur',
        clearable=False,
    ),
    dcc.Store(id='reponse'),
    dcc.Store(id='clicked-nodes', data=[]),
    cyto.Cytoscape(
        id='cytoscape-graph',
        layout={'name': 'cose'},
        style={'width': '100%', 'height': '500px'},
        elements=[],
    )
    ])

@app.callback(
    Output('cytoscape-graph', 'elements'),
    Output('reponse', 'data'),
    Input('generate-btn', 'n_clicks'),
    State('parcours-option', 'value'),
    allow_duplicate=True,
    prevent_initial_call=True,
)

def generer_graphe_dash(n_clicks, type_parcours):
    nb_noeuds = random.randint(5, 10)
    proba = 0.3
    option_poids = False

    G = generer_graphe(nb_noeuds, proba, option_poids)
    
    if type_parcours == 'profondeur':
        chemin = parcours_profondeur(G)
    if type_parcours == 'largeur':
        chemin = parcours_largeur(G)
    
    elements = conversion_nx_cytoscape(G, option_poids)
    
    return elements, chemin

app.clientside_callback(
    """
    function(tapped_node, clicked_nodes, elements, parcours) {
        if (!tapped_node) return window.dash_clientside.no_update;

        const node_id = tapped_node.id;
        if (!clicked_nodes.includes(node_id)) {
            clicked_nodes.push(node_id);
        }
        return parcours_complet(clicked_nodes, elements, parcours);
    }
    """,
    Output('clicked-nodes', 'data'),
    Input('cytoscape-graph', 'tapNodeData'),
    State('clicked-nodes', 'data'),
    State('cytoscape-graph', 'elements'),
    State('reponse', 'data'),
    prevent_initial_call=True
)


if __name__ == "__main__":
    app.run(debug=True)




    
# pour les noeuds interactifs
# si on clic et la comparaison de parcours ok 
#   -> noeud change de couleur
#   -> you cant click on it anymore
#
# si on clic et il y a une erreur dans le parcours
#   -> node becomes red and fades back to orange
#


# ajouter un call back ou si clicked-nodes sont = a la taille du graphe on vérifie si le parcours est corrct
# une comparaison simple de deux tableaux

# ajouter un bouton retour pour retirer un noeud de data en cas d'Erreur de l'utilisateur