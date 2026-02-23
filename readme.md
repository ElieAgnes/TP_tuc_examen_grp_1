
# Rendu TP - Groupe 1 :

- Elie Agnès

-

-

-

### Installation : 
*Version de python nécessaire : [J'en sais rien en faite, ça marche sur mon PC et c'est un TP après tout]*

Créer un environnement python :

```bash
python  -m  venv  venv
```
Démarrer  l'environnement python :
```bash
venv\Scripts\activate
```
Installation  de  dépendance (le requirements  est  là  pour  faire  joli)
```bash
pip install fastapi locust pytest uvicorn coverage httpx pytest-mock pytest-profiling pylint sqlalchemy pydantic
```

Execution  du  code
```bash
uvicorn main:app --reload
```
### Test du code
Après  avoir  démarré,  on  essaye  avec  ces  données,  d'abord créer deux users avec
`POST | /trainers/`
```json
{
	"name":"Gamin Farouk",
	"birthdate": "2000-10-15"
}
```

`POST  |  /trainers/`
```json
{
	"name":"Silver",
	"birthdate": "1999-11-12"
}
```
On  ajoute  les  pokémons  aux  dresseurs  :
`POST  |  /trainers/1/pokemon`
```JSON
{
	"api_id" : 19
}
```
`POST  |  /trainers/2/pokemon`
```JSON
{
	"api_id" :
}
```


On  fait se battre les  pokémons  des dresseurs  :
`POST  |  /fight/1/2/`
```JSON
	{
		"winner":  {
			"name":  "Silver",
			"birthdate":  "1999-11-12",
			"id":  2,
			"inventory":  [],
			"pokemons":  [
				"api_id":  152,
				"custom_name":  null,
				"id":  2,
				"name":  "chikorita",
				"trainer_id":  2
			}]
		},
	"is_tie":  false
	}```

