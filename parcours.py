import heapq

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
            
        