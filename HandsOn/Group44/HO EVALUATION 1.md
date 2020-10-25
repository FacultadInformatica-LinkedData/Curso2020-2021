Group 44
    General
    Analysis
        - The analysis.html file does not contain the resource naming strategy, just a base URI.
        - Use a domain in your resource naming strategy that is not the one given by default in Protege.
        - URIs should not contain information that may change over time such as years or months.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Object properties should be named in singular.
        - dbpedia:province is a property; you should use dbpedia:Province.
        - Identifiers are not numbers.
        - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
        - In the ontology you are mixing labels in Spanish and English.
    RDF generated
        - Measurement values are floats, not integers. You can see it in the generated data.
        - The RDF file does not contain individuals with labels.
