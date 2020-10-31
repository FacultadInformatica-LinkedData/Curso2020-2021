Group 17
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - The analysis.html file does not contain the resource naming strategy.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Use Protege to define your ontology to avoid mistakes.
        - esPuntoMuestreo and esMedida seem to be properties, not classes.
        - Check that all class names start with capital letter.
        - Datatype properties are not correctly defined. This is not the correct way of defining the different valido and hora.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - The RDF file does not use the class and property URIs defined in the ontology.
        - Some URIs are not correctly defined.
        - Boolean data values are not encoded properly.
        - Two different individuals have the same URI because the naming strategy applied does not ensure uniqueness.
