Group 04
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - The analysis.html file does not contain the resource naming strategy.
        - Spatial coordinates are numerical values, not an entity that can be linked. That is, even if in the application you relate entities by their spatial distance, the datasets won't be linked.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - The namespace of the ontology terms must not be a domain name.
        - Use Protégé to define the ontology. Properties are repeated, comments do not correspond to the axioms.
        - In the ontology you are mixing labels in Spanish and English.
        - Correct: "Address"
        - It is a good practice to name classes in singular and not plural.
        - Some ranges of the datatype properties are not correct.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - Individuals have no type.
        - Date values are not encoded properly.
        - Datatypes are missing.
        - Verify that the class and property names used in the RDF data are the same as those used in the ontology.
        - The RDF file does not contain individuals with labels.
        - Names are not integers.
        - Solve the character encoding issues.
