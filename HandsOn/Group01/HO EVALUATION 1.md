Group 01
    General
        - The hands-on directory does not follow the required structure.
        - The self-assessment files do not reflect the reality of the work.
    Analysis
        - The datasetRequirements.html file is not correctly formatted.
        - The datasetRequirements.html file does not state how the selected datasets satisfy the requirements.
        - The applicationRequirements.html file is not correctly formatted.
        - The applicationRequirements.html file does not describe clearly what is the purpose of the application.
        - The applicationRequirements.html file does not include a description of the user interface.
        - The analysis.html file does not contain the analysis of the selected datasets.
        - The analysis.html file does not contain the license of the dataset to be generated.
        - The analysis.html file does not contain the resource naming strategy.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - The ontology does not follow a resource naming strategy.
        - The subclass-of relationship is not used correctly. That property is an inheritance property; therefore, all the members of the subclass must also be members of the class. 
        - The ontology does not contain properties.
        - Even if IRIs allow to use accented words, I would not  create URIs with accents. You can leave the accents in the description of the resource, though.
        - It is not a good practice to use in the ontology file name a version number. The reason for this is that if you change the version of the ontology, all the URIs related to the base URI will change.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - Two different individuals have the same URI.
        - The RDF file does not use the class and property URIs defined in the ontology.
        - The RDF file does not contain individuals with labels.
        - Individuals have no type.
        - Datatypes are missing.
