# Algo-graphes (en cours)


## Description / Overview
Ce projet est un programme python permettant la pratique de parcours d'algorithmes tels que le parcours en largeur, le parcours en profondeur... Le programme propose des graphes aléatoirement générés avec NetworkX pour visualiser et pratiquer des parcours plus facilement.

This project is a Python program designed to help users practice graph traversal algorithms such as breadth-first search (BFS), depth-first search (DFS), and more.
The program generates random graphs using NetworkX, making it easier to visualize and practice traversals interactively.

---

## Pourquoi ? / Why?
L’idée du projet est d’aider les personnes souhaitant pratiquer leur compréhension des parcours de graphes. La pratique est essentielle pour solidifier les connaissances des algorithmes de graphes, mais peu d’exercices interactifs sont disponibles.
Ce projet a donc pour objectif de générer automatiquement des graphes et de permettre à l’utilisateur de s’exercer en testant ses réponses à l’aide d’un système interactif. Il devient ainsi possible de pratiquer différents types d’algorithmes sans limitation sur la quantité de ressources.

## Utilisation / Usage

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

## onctionnalités / Features
- [x] Génération de graphes aléatoires
- [x] Conversion de graphes Networkx vers Dash Cytoscape
- [x] Visualisation de graphe avec Dash Cytoscape
- [x] Interface interactive
- [x] Exploration des graphes interactive
- [ ] retour arrière en cas d'erreur
- [x] parcours en profondeur
- [ ] parcours en largeur
- [ ] algorithme Prim
- [ ] algorithme Kruskal
- [ ] algorithme Dikjstra
