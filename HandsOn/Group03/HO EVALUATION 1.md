Group 03
    General
    Analysis
        - The datasetRequirements.html file does not identify the entities in the selected datasets that can be linked with entities in other datasets.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
        - The analysis.html file does not contain the resource naming strategy.
        - URIs cannot have two hashes (#).
    Ontology
        - The ontology file must be in the Turtle (.ttl) format.
        - Use Protégé to create the ontology, it has syntax errors.
        - The same name cannot be used in two different properties.
        - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
    RDF generated
        - Solve the character encoding issues.
        - Classes are used as properties.
        - Incorrect values are generated ($LibraryAdministration).
