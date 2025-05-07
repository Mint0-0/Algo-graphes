# Algo-graphes (en cours)


## Description
Ce projet est un programme python permettant la pratique de parcours d'algorithmes tels que le parcours en largeur, le parcours en profondeur... Le programme propose des graphes aléatoirement générés avec NetworkX pour visualiser et pratiquer des parcours plus facilement.

## Utilisation

pour pouvoir rouler le projet, certaines librairies sont nécéssaires. Sous Windows l'installation des librairies peut se faire comme ceci:

```
pip install dash dash-cytoscape networkx matplotlib plotly
```

Par la suite pour lancer le programme dans un terminal il suffit de faire cette commande
``` 
python3 graphe.py
```

Le texte 
```
Dash is running on http://127.0.0.1:8050/
```
devrait apparaître et en suivant le lien une page HTML vous permettant de générer les graphes devrait apparaître.

## Fonctionnalités
- [x] Génération de graphes aléatoires
- [x] Conversion de graphes Networkx vers Dash Cytoscape
- [x] Visualisation de graphe avec Dash Cytoscape
- [ ] Interface interactive
- [ ] Exploration des graphes interactive