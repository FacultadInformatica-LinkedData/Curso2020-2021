# Hands-on assignment 4 – Self assessment

## Checklist

**Every RDF file:**

- [X] Uses the .nt extension
- [X] Is serialized in the NTriples format
- [X] Follows the resource naming strategy
- [X] Uses class and property URIs that are the same as those used in the ontology

**Every URI in the RDF files:**

- [X] Is "readable" and has some meaning (e.g., it is not an auto-increased integer) 
- [X] Is not encoded as a string
- [X] Does not contain a double slash (i.e., “//”)

**Every individual in the RDF files:**

- [X] Has a label with the name of the individual
- [X] Has a type

**Every value in the RDF files:**

- [X] Is trimmed
- [X] Is properly encoded (e.g., dates, booleans)
- [X] Includes its datatype
- [X] Uses the correct datatype (e.g., values of 0-1 may be booleans and not integers, not every string made of numbers is a number)

## Comments on the self-assessment

### v1
* Initial mappings and NTriples file uploaded.
### v2
* Included the datatypes of the literals.
### v3
* Changed _measuredAt_ property mapping in the _.yml_ document since it was located in the wrong TriplesMap.
* Included the TriplesMap corresponding to the new _magnitudes_ dataset.
### v4
* Placed correct datatypes to string codes.
* Included the _measuredMagnitude_ property to link both Measurement and Magnitude entities.
* Included Wikidata links with _owl:sameAs_ properties.
* Included properties _rdfs:subClassOf_ that were written in the ontology but not in the mappings.
### v5
* Rewrite mappings with missing property _inStreet_.