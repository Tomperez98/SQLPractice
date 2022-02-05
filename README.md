# Documentation
## Setup Steps
* Our first database we will be working on is [Pagila](https://dataedo.com/samples/html/Pagila/doc/Pagila_10/modules.html)
To download the file go to https://github.com/devrimgunduz/pagila/blob/master/pagila-insert-data.sql click in `Download` and then `right-click` -> `save page as...`. This file **MUST** be moved into `sql_queries/` folder.

Or run the following command `curl -o sql_queries/pagila_database.sql https://raw.githubusercontent.com/devrimgunduz/pagila/master/pagila-insert-data.sql`

## Let's work
To fullfill the database go to the root of the folder and run:
* `docker-compose up`

To stop the docker run:
* `docker-compose stop`

To clean docker run:
* `docker system prune -a --volumes`
