# Algo-graphes (en cours)


## Description / Overview
Ce projet est un programme python permettant la pratique de parcours d'algorithmes tels que le parcours en largeur, le parcours en profondeur... Le programme propose des graphes aléatoirement générés avec NetworkX pour visualiser et pratiquer des parcours plus facilement.

This project is a Python program designed to help users practice graph traversal algorithms such as breadth-first search (BFS), depth-first search (DFS), and more.
The program generates random graphs using NetworkX, making it easier to visualize and practice traversals interactively.

---

## Pourquoi ? / Why?
L’idée du projet est d’aider les personnes souhaitant pratiquer leur compréhension des parcours de graphes. La pratique est essentielle pour solidifier les connaissances des algorithmes de graphes, mais peu d’exercices interactifs sont disponibles.
Ce projet a donc pour objectif de générer automatiquement des graphes et de permettre à l’utilisateur de s’exercer en testant ses réponses à l’aide d’un système interactif. Il devient ainsi possible de pratiquer différents types d’algorithmes sans limitation sur la quantité de ressources.

The goal of this project is to help users practice and deepen their understanding of graph traversal algorithms. Practice is essential for mastering graph algorithms, but interactive exercises are scarce.
This tool generates random graphs and allows users to test their answers interactively, making it possible to train various algorithms without any limitations on the amount of ressources.

---

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
devrait apparaître et en suivant le lien une page HTML vous permettant de générer et d'interagir avec les graphes devrait apparaître.



To run the project, certain libraries are required. On Windows, the installation can be done as follows:
```
pip install dash dash-cytoscape networkx matplotlib plotly
```
Then, to launch the program from a terminal, simply run the following command:

```
python3 graphe.py
```
The following message should appear:

```
Dash is running on http://127.0.0.1:8050/
```
By opening that link in a browser, an HTML page will appear allowing you to generate and interact with graphs.

---

## Fonctionnalités / Features
- [x] Génération de graphes aléatoires / Random graph generation
- [x] Conversion de graphes Networkx vers Dash Cytoscape / NetworkX to Dash Cytoscape graph conversion
- [x] Visualisation de graphe avec Dash Cytoscape / Graph visualization with Dash Cytoscape
- [x] Interface interactive / Interactive interface
- [x] Exploration des graphes interactive / Interactive graph exploration
- [ ] Retour arrière en cas d'erreur / Undo feature for errors
- [x] Parcours en profondeur / Depth-first search (DFS)
- [ ] Parcours en largeur / Breadth-first search (BFS)
- [ ] Algorithme Prim / Prim’s algorithm
- [ ] Algorithme Kruskal / Kruskal’s algorithm
- [ ] Algorithme Dikjstra / Dijkstra’s algorithm
