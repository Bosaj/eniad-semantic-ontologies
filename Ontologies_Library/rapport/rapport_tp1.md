# TP1 : Construction d'un petit réseau sémantique avec Protégé

## Introduction
Ce TP a pour but de vous familiariser avec l’interface de Protégé et de vous guider dans la création d'une ontologie simple représentant un domaine choisi.

## Objectifs
- Se familiariser avec l’interface de Protégé.
- Créer une ontologie simple représentant un domaine donné.
- Utiliser les relations hiérarchiques et les propriétés pour structurer les connaissances.

## 1. Choix du domaine
**Domaine sélectionné** : Famille  
**Justification** : domaine simple et riche en relations hiérarchiques (Parent/Child).

## 2. Identification des concepts
- Concepts clés :
  - `Person` (classe racine)
  - `Parent` (sous-classe de `Person`)
  - `Child` (sous-classe de `Person`)

## 3. Création de l’ontologie
1. Création d’une nouvelle ontologie (IRI : `http://www.example.org/family`)  
   ![Figure 1 – Nouvelle ontologie](figures/figure1_creation_ontology.png)  
   *Figure 1 : Fenêtre de création d’une nouvelle ontologie dans Protégé*

2. Définition des classes (`Person`, `Parent`, `Child`)  
   ![Figure 2 – Classes définies](figures/figure2_classes.png)  
   *Figure 2 : Vue « Classes » dans Protégé*

3. Création des propriétés  
   - `hasChild` (domain = Parent, range = Child, inverseOf = hasParent)  
   - `hasParent` (domain = Child, range = Parent)  
   - `hasAge` (datatype property, domain = Person, range = xsd:integer)  
   ![Figure 3 – Propriétés](figures/figure3_properties.png)  
   *Figure 3 : Éditeur de propriétés de Protégé*

4. Instanciation des individus (`Jean`, `Marie`, `Paul`)  
   ![Figure 4 – Individus](figures/figure4_individuals.png)  
   *Figure 4 : Création d’individus dans Protégé*

## 4. Visualisation et vérification
- Utilisation du reasoner HermiT pour vérifier la cohérence  
  ![Figure 5 – Raisonneur](figures/figure5_reasoner.png)  
  *Figure 5 : Résultats du raisonnement dans Protégé*

- Vue graphe pour visualiser les relations  
  ![Figure 6 – Graphe](figures/figure6_graph.png)  
  *Figure 6 : Visualisation en graphe des classes et propriétés*

## 5. Ajout de restrictions (optionnel)
- Ex. : `Child` doit avoir au moins un parent (`minCardinality 1` sur `hasParent`)  
  ![Figure 7 – Restriction](figures/figure7_restriction.png)  
  *Figure 7 : Ajout d’une restriction sur la propriété*

## 6. Import d’ontologies existantes (optionnel)
- Exemple : import de la partie « person » de FOAF ou WordNet pour enrichir `Person`.  

## 7. Raisonnement ontologique et requêtes SPARQL (optionnel)
- Lancement de requêtes pour extraire, par exemple, tous les parents de `Paul`.

---

**Fichiers fournis** :  
- `family_fixed.owl` : ontologie OWL.  
- `rapport_tp1_complete.md` : ce rapport (avec placeholders pour figures).
