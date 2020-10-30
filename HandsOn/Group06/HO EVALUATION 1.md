Group 06
    General
    Analysis
        - Regarding the resource naming strategy, URIs with more than one hash are not allowed.
        - Do not use a hash and after it a slash in URIs.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - In cases such as this with the types of residues, where the potential values are an enumeration, usually what is done is to define a class (Residue) and the different types as instances of the class. This is, in fact, how you are doing it in the RDF file.
        - A street with a number is not a street, it is an address in such street.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - If there were more than one bin in the same street with different street number, the naming strategy does not ensure uniqueness.
        - URIs are encoded as strings.
        - The RDF file does not use the class and property URIs defined in the ontology.
