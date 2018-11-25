## Airflow runs in Docker Container

#### Prerequisites

a. Create a fresh virtualenv w/ Python 3.6 and also install docker and docker compose.

b. Run `make init` to set up the environment and install all the prerequisites.

c. Run `make test` to make sure all of the smoke tests are passing without any issues

d. Run `make run` to bring up the airflow server:
* Once this command is executed, the airflow server should be visible at http://localhost:8080
