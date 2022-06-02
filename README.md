# Amusez-vous avec Flask

# Getting started

* Lancer la commande : 

```
pip install -r requirements.txt
```

* Sous windows télécharger cURL

```
https://curl.se/windows/
```


##

Commandes gérées :

```
curl --request GET --url "http://localhost:8080/notes/Benjamin"
curl --request GET --url "http://localhost:8080/moyenne/Benjamin"
curl --request GET --url "http://localhost:8080/eleves"
curl --request POST --url "http://localhost:8080/notes/François?note=20"
```