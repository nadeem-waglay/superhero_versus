# superhero_versus
A Top Trump style game api using open superhero API

### Run Locally
To Run locally : 
```
docker build --tag python-django .
```

and then,
```
docker run --publish 8000:8000 python-django
```



## Comparing Superheros
Super heros can be compared by the general end point : 
 
 `http://localhost:8000/api/superhero_versus/<HERO_A>/<HERO_B>/<STAT>`

 where `HERO_A` and `HERO_B` are the two hero's to compare and the stats you can compare them on are:
 - Intelligence
 - Strength
 - Speed
 - Durability
 - Power
 - Combat

 ### Examples:

http://localhost:8000/api/superhero_versus/joker/batman/intelligence

http://localhost:8000/api/superhero_versus/spider-man/wolverine/combat

http://localhost:8000/api/superhero_versus/batman/Ironman/combat
