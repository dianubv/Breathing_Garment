

docker run --device="/dev/ttyACM0"

# Breathing Garment

This project is a Docker-based solution to stock data from a microcontroler. It is used for a breathing garment which return tension variations during respiration. 
It includes a MySQL database and Python applications to ask user information, read serial data from a microcontroller, save it as CSV files and provide an API to search names in the database and CSV files.


## Prerequisites

To run this project, you must have the following installed on your system:

- Docker
- Docker Compose

## Getting Started


To use this application, you will need to have Docker installed on your system.
Installation

    1. Clone this repository to your local machine.
    2. Run `docker-compose build` to build the Docker images.
    3. Run `docker-compose up` to start the containers.
    
## Usage

Once the Docker containers are running, you can use the following scripts to interact with the application:

    - `run.sh` : to launch the data reccord. This program demands you to write your name, first name and birth date.
    - `api.sh`: Provides an API to search for name in the database and CSV files.


## Files

The project includes the following files:

- `docker-compose.yml`: This file creates a MySQL Docker container and a Python Docker container.
- `Dockerfile`: This file contains instructions for building the Docker image.
- `hardware_to_db.py`: This program reads data from a microcontroller via Serial and saves it to CSV files in the `dataframes` folder.
- `info_user.py`: This program prompts the user for information and stores it in a MySQL database.
- `run.sh`: This script launches `hardware_to_db.py` and `info_user.py` programs.
- `api.py`: This program provides an API to search for data in the CSV files and the MySQL database.
- `api.sh`: This scipt launches `api.py` program.

