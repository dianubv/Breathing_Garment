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


<!--  -->
A la fin de la creation du docker on execute api.py, 
- verifier que l'api fonctionne avec un Hello world
- plusieurs commandes y sont a tester (avec uvicorn)

quand on sait que api.py s'execute 
il serait interessant de remplacer le contenu de api.py par contenu dans le fichier text : aide_Diane/nico.py 

si l'api est accessible alors on pourra mettre dans la boucle infinie l'information de hadware_to_db.py
il serait alors interessant
 de la faire une liste to numpy array et l'envoyer a la base de donnée avec pandas comme dans nico2.py






