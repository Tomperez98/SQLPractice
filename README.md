# Documentation
## Setup Steps
- 1) The first command you want to run is `pre-commit install`. This setups git in your repo to check code quality before every commit is made

## Let's work
To fullfill the database go to the root of the folder and run:
* `docker-compose -f .prodcontainer/docker-compose.prod.yml up -d`

To stop the docker run:
* `docker-compose -f .prodcontainer/docker-compose.prod.yml stop`

To clean docker run:
* `docker system prune -a --volumes`
