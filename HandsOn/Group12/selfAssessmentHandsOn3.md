#Hands-on assignment 3 – Self assessment#

##Checklist##

**Every resource described in the CSV file:**

- [X] Has a unique identifier in a column (not an auto-increased integer)
- [X] Is related to a class in the ontology

**Every class in the ontology:**

- [X] Is related to a resource described in the CSV file

**Every column in the CSV file:**

- [X] Is trimmed
- [X] Is properly encoded (e.g., dates, booleans)
- [X] Is related to a property in the ontology

**Every property in the ontology:**

- [X] Is related to a column in the CSV file

##Comments on the self-assessment##
- Since our csv was a transformed xlsx file it had some empty columns and rows as well as rows that had the total sum of scooters in each District and a column with the total sum of scooters in a neighbourhood and we deleted all of them to clean our dataset. Also we created a Place column and an Availability column as well as its respective URI columns.
- Our ontology was not built correctly so we decided to rewrite it and now it makes much more sense and it fits perfectly with our CSV file.
- Now our ontology has a Place class which has two subclasses: District and Neighbourhood.
- Now our ontology has a Availability class so that we can know the number of scooters available in a Place (District Neighbourhood) filtered by Company.
