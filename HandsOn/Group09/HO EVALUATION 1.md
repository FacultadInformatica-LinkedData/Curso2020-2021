Group 09
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Sex and gender are not the same thing.
        - If you are only going to define the dateTime for the Time class, you can avoid having that class and directly define a datatype property with dateTime as range.
        - In cases such as this with the types of persons, accidents, etc., where the potential values are an enumeration, usually what is done is to define a class and the different types as instances of the class. 
    RDF generated
        - injuryStatus is not an integer.
