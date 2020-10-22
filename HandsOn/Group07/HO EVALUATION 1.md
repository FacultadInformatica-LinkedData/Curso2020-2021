Group 07
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Do not write class names in capitals; only the first letter or CamelCase.
        - If the denominación is a name, I don't understand why it does have more properties.
        - It is not clear what the OBJECTID class refers to.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - The instances of denominación and objectId seem to be duplicated but with different URIs.
        - Solve the character encoding issues.
        - tieneSentido has as range a class, not a string.
        - If all the lines have two sentidos, it is better to represent that directly in the ontology.
        - Datatypes are missing.
        - There are sentidos with length and speed cero.
