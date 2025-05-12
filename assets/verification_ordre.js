 /**
  * filtre elements pour avoir uniquement les noeuds et vérifie si tous les noeuds du graphes ont été
  * cliqué. Affiche un message si c'est le cas
  * @param {} clicked_nodes tableau contenant les noeuds déjà cliqué
  * @param {*} elements éléments du graphes
  * @returns la liste des noeuds cliqué
  */
 function parcours_complet(clicked_nodes, elements) {
    let noeuds = elements.filter(el => el.data && el.data.id && !el.data.source && !el.data.target)     // ignore les aretes
                            .map(el => el.data.id);  // on veut juste l'id du noeud pour plus tard vérifier le parcours

    if (clicked_nodes.length === noeuds.length) {
        alert("parcours complet");  
    }
    return clicked_nodes;
}