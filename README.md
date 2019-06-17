### SPARKIFY ETL 
#### Pipeline to load json data into a PSQL DB for further analysis

#### Project Overview

Music company sparkify generate JSON logs that cover how songs are played in their app. This dataset is joined with an open source songs and artist JSON collection so data analysts can identify trends in song plays.

#### App Architecture
![App Architecture Diagram](diagrams/sparkify_app.jpg)

#### Database Schema 
![(Database Schema)](diagrams/sparkify_sql.jpg)

#### Setup

* Ensure psql and python3 are installed

* From inside the project directory create a python 3 virtual environment called venv_psql_sparkify
  
* Load the virtual environment and run pip install -r requirements.txt
  
* Run ./etl_exec.sh. This script will drop the existing tables in the schema and then recreate them. From there the python application will populate the tables with the data from the data/ directory. 

#### Additional Steps

* Performance testing with further denormalized tables, ideally with a bigger dataset or in an environment with low ram to identify bottlenecks
* Have db and python scripts execute inside containers
* Developing unit tests alongside code to make code more production ready and increase documentation
* Incorporate the code into a jupyter server so results and dataframes can be reviewed more easily

