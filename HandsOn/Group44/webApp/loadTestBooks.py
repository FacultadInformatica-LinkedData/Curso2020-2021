# Esto es para meter varios libros en la BDD para poder tenerlos y hacer pruebas a partir de ellos :D

import requests
url = 'http://localhost:4000/api/books/add_book'


books = [{
            "ISBN": 9788097647957,
	    "title": "Titulo_1",
	    "author": "Autor_1",
	    "edition": 1,
	    "publisher": "Editorial_1"
        },
        {
            "ISBN": 9788593174827,
	    "title": "Titulo_2",
	    "author": "Autor_2",
	    "edition": 1,
	    "publisher": "Editorial_2"
        },
        {
            "ISBN": 9789687788647,
	    "title": "Titulo_3",
	    "author": "Autor_3",
	    "edition": 1,
	    "publisher": "Editorial_3"
        },
        {
            "ISBN": 9781200706077,
	    "title": "Titulo_4",
	    "author": "Autor_4",
	    "edition": 1,
	    "publisher": "Editorial_4"
        },
        {
            "ISBN": 9781074029616,
	    "title": "Titulo_5",
	    "author": "Autor_5",
	    "edition": 1,
	    "publisher": "Editorial_5"
        },
        {
            "ISBN": 9783238088170,
	    "title": "Titulo_6",
	    "author": "Autor_6",
	    "edition": 1,
	    "publisher": "Editorial_6"
        },
        {
            "ISBN": 9782953184419,
	    "title": "Titulo_7",
	    "author": "Autor_7",
	    "edition": 1,
	    "publisher": "Editorial_7"
        },
        {
            "ISBN": 9787040617528,
	    "title": "Titulo_8",
	    "author": "Autor_8",
	    "edition": 1,
	    "publisher": "Editorial_8"
        },
        {
            "ISBN": 9786437867768,
	    "title": "Titulo_9",
	    "author": "Autor_9",
	    "edition": 1,
	    "publisher": "Editorial_9"
        },
        {
            "ISBN": 9788945045676,
	    "title": "Titulo_10",
	    "author": "Autor_10",
	    "edition": 1,
	    "publisher": "Editorial_10"
        },
        {
            "ISBN": 9786629631917,
	    "title": "TituloRepe",
	    "author": "AutorTitRepe_1",
	    "edition": 1,
	    "publisher": "Editorial_11"
        },
        {
            "ISBN": 9782637553043,
	    "title": "TituloRepe",
	    "author": "AutorTitRepe_2",
	    "edition": 1,
	    "publisher": "Editorial_12"
        }
]

count = 0
for x in books:
    res = requests.post(url, json = x)
    if(res.status_code < 200 or res.status_code >= 300):
        print("Book", count, ":", res.text)
    else:
        print("Book", count, ": All gucci!")
    count += 1

url = 'http://localhost:4000/api/books/armadilloPuesNose'
res = requests.get(url)
print(res.status_code)
