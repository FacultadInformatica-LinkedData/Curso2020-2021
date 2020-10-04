# Hands-on assignment 3 – Self assessment #

## Checklist ##

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

## Comments on the self-assessment ##

### v1
* Two JSON documents are uploaded since we had two different types of datasets.
* Data refining actions taken:
  * Removing redundant columns (province, town; every data is from Madrid).
  * Formatting numeric columns (station or magnitude codes, dates, values).
  * Splitting one-full row (with up to 30 magnitude measured) to up to 30 rows each.
  * Filling down the values for the new rows created.
  * Transposing data in order to merge the different types of datasets.
  * Normalize the columns of data and merging the datasets.