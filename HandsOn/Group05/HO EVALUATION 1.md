Group 05
    General
        - The hands-on directory does not follow the required structure.
    Analysis
        - Spatial coordinates are numerical values, not an entity that can be linked. That is, even if in the application you relate entities by their spatial distance, the datasets won't be linked.
        - The resource naming strategy is not correct. Do not follow the "JSON view" on the data. For example, the URI of a street should not depend on a specific station; if so, you will be defining different URIs for the same resource.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Check the datatypes. Latitude and longitude are not strings.
    RDF generated
        - The RDF file does not follow the resource naming strategy.
        - It could happen that two individuals have the same URI because the naming strategy does not ensure uniqueness (e.g. two coordinates with the same latitude but different longitude)..
        - The URI of an individual should be "readable" and have some meaning.
            An auto-increased integer does not satisfy this.
        - Datatypes are missing.
        - Solve the character encoding issues.
        - Street names should be better formatted.
