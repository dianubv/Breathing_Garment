A docker compose with 2 dockers :
    -Arduino Docker to receive data from the stretch sensor
    -mySQL Docker to stock data


hardware_to_db.py :
    -connect with the ESP32
    -receive data from the sensor 
    -make "table" with name, time and all sensor's data


database.py :
    -connect to the database create in the docker
    -add "table" on a new table

api.py :
    -connected to the db
    -user's interface
    -return all data of "name"
    -return all data of "time"
    -later : graph

todo 
debug hardware to read good value on esp32
il est deja possible que le pont diviseur de tension resolve le probleme
- possible problems
    - courrant pas suffisant alors que arduino uno si
        -    - envoyer plusieurs pins 5v a la sortie (plus de courrant)

    - pont diviseur de tension mal fait


savoir que la difference entre les deux main.cpp s est un lissage de la sortie, (on effectue une moyenne entre deux lectures du pin A0)

il serait interessant de regarder la tension de sortie du ohmetre sur 20k (position lors du test reussi) 
est ce proche du 5v de la arduino ou plus 

<!--  -->
A la fin de la creation du docker on execute api.py, 
- verifier que l'api fonctionne avec un Hello world
- plusieurs commandes y sont a tester (avec uvicorn)

quand on sait que api.py s'execute 
il serait interessant de remplacer le contenu de api.py par contenu dans le fichier text : aide_Diane/nico.py 

si l'api est accessible alors on pourra mettre dans la boucle infinie l'information de hadware_to_db.py
il serait alors interessant
 de la faire une liste to numpy array et l'envoyer a la base de donnée avec pandas comme dans nico2.py






