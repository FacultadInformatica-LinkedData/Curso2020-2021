# MadScooters: Find your scooter!

MadScooters is a web application that allows users to search for a scooters' company availability filtering by District and Neighbourhood.



### Libraries and plugins

MadScooters uses a number of python libraries and plugins to work properly:

* [rdflib](https://github.com/RDFLib/rdflib) - A python library used for rdf operations like querying or accessing the components of a knowledge graph.
* [SPARQLWrapper](https://pypi.org/project/SPARQLWrapper/) - A wrapper around a SPARQL service. It helps in creating the query URI and converting the result into a more manageable format.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework written in Python, its main purpose is to create web applications easily and quickly.
* [Flask CORS](https://flask-cors.readthedocs.io/en/latest/) - A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
* [pandas](https://pandas.pydata.org/) - A library made for data analysis and data manipulation, built on top of the Python programming language.


### Installation

MadScooters requires a server and a client to run on Ubuntu.

Install the required dependencies:
```sh
$ sudo apt install virtualenv 
$ pip3 install rdflib
$ pip3 install SPARQLWrapper
$ pip3 install pandas
$ pip3 install flask
$ pip3 install -U flask-cors
```
*If pip3 does not exist in your ubuntu version, substitute it with pip.

Install and run the server:
* The following commands have to be run on the MadScooters directory.
```sh
$ cd ./Backend
$ chmod +x init.sh
$ ./init.sh
```

Start the user interface:
* Go to the ./Frontend directory and click on the index.html file.

# Enjoy the application!