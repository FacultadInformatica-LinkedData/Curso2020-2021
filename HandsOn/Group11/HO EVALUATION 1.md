Group 11
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Do not create the ontology by hand. Use Protege to avoid errors.
        - The same property is defined multiple times.
        - Correct: distric -> district.
        - District codes are not integers.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - Two different individuals have the same URI because the naming strategy applied does not ensure uniqueness.
        - The RDF file does not use the class and property URIs defined in the ontology.
        - Datatypes are missing.
        - xsd:time is not correctly used.
        - isStart is incorrectly duplicated.
