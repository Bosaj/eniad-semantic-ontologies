# Academic Curriculum & Laboratory Guide 📂

This guide presents the complete educational structure, competency mapping, and lab sequence for **ENIAD Semantic Web & Knowledge Ontologies**.

---

## 📑 Curriculum Matrix

| Module / Lab | Topic | Deliverables & Artifacts |
|---|---|---|
| `Partie 1: Théorie` | Knowledge Representation | Stanford 101 ontology lifecycle, conceptualization, competency definitions |
| `Partie 2: Protégé` | Taxonomy & Classes | Hierarchy authoring, object and data properties, domain & range constraints |
| `Partie 3: Formalismes` | OWL 2 & Description Logics | Axiomatic constraints, disjointness, universal and existential quantifiers |
| `Partie 4: Raisonnement` | DL Reasoners & SWRL | Automated subsumption, consistency verification using HermiT and Pellet |
| `Partie 5: SPARQL` | Semantic Queries | SELECT, CONSTRUCT, ASK queries, federated queries, knowledge extraction |
| `Library Ontology` | Complete Deliverable | `tp1_library.owl`, `tp1_library_cleaned.owl`, `TP1_Library_Report.pdf` |


---

## 📚 Ontology Engineering Life Cycle

1. **Competency Questions Definition**: Formulating user queries that the knowledge model must answer.
2. **Class & Property Hierarchy authoring**: Designing taxonomic subsumption (`rdfs:subClassOf`) and property domains/ranges.
3. **Formal Axiomatization**: Disjoint classes, inverse properties, functional and transitive characteristics.
4. **Automated Reasoning & Consistency Checking**: Invoking HermiT and Pellet reasoners to infer implicit relationships and detect contradictory assertions.
5. **SPARQL Endpoint Execution**: Executing pattern-matching graph queries over the ontology repository.

