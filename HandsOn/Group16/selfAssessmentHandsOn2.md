# Hands-on assignment 2 – Self assessment #

## Checklist ##

**Analyse Data Set**:

- [X] Analyse the data (quantities, value ranges, etc.)
- [X] Analyse the schema of the data

**Analyse Licensing of the Data Source**:

- [X] Analyse who is the publisher of the dataset and its rightsholder, as well as the licence of the dataset
- [X] Define the potential license to be used for the dataset to be generated.

**Define Resource Naming Strategy**:

- [X] Define the resource naming strategy to be followed for the ontology and the data to be generated

**Develop Ontology**:

- [X] Develop a lightweight ontology that includes the classes and properties to be used with the dataset

## Comments on the self-assessment ##

### v1
* Initial version of the ontology developed, 2 object properties, 8 data properties and 2 classes.
### v2
* Changed object property _locatedAt_ by defining class _Station_ as subclass of _schema:Place_.
### v3
* Reduced data properties to 4 in order to lightweight the ontology and making the mapping easier.
### v4
* Modified _csv-shortened.csv_ document in order to restore _date_ column, which was lost in the shortening process.
### v5
* Included _Magnitude_ entity, used for identifying each magnitude with its name and code.
### v6
* Added _District_ and _Street_ entities, as well of their corresponding data and object properties, in order to accomplish the linking of the data with other datasources.
### v7
* Redefined two properties with multiple domain targets to an owl:unionOf classes, due to the Oops! evaluation.
* Included _inStreet_ property, which was actually missing.