# Rock in Rio (2022) Twitter Scrapper - DEPRECATED due to Twitter recent API changes.
---
## OBJECTIVES: 
1. Get data of the hashtag #RockinRio2022 (or others) from Twitter.
2. Create an index on Elasticsearch (running on Docker) and populate with the hashtag data.
3. Create a collection in MongoDB (running on Docker) and populate with the hashtag data.
---
## Tweets Data Schema:
The bellow JSON is an example of the documents in the Elasticsearch and MongoDB.
```json
{
    "created_datetime":, 
    "url":, 
    "like_count":, 
    "reply_count":, 
    "retweet_count":, 
    "hashtags":, 
    "language":, 
    "source":, 
    "content":
}
```
---
# How to use this project:
##### Requiriments: Have [Docker](https://www.docker.com) and [Docker Compose](https://docs.docker.com/compose/install/#install-compose) installed.

---
1. Create a file named "**.env**", this file should be equal to the "**.env.example**" file. You can just copy the file (use default variables) or change the variables.
2. Create a folder that Elasticsearch can store data:
```sh
mkdir es_data && chown 1000:1000 es_data
```
3. Execute the bellow command to create the Docker containers of Elasticsearch and MongoDB in background:
```sh
docker compose up -d
```
4. Install the Python dependencies:
```sh
pip install -r requirements.txt
```
5. Execute the main Python file to populate Elasticsearch and MongoDB:
```sh
python3 main.py
```
---

## Additional commands:

#### Show all containers running:
```sh
docker ps
```
#### Stop the project containers:
```sh
docker compose down
``` 
#### Executes a command inside a container:
```sh
docker exec <container name/id> <command>
```
#### Show a container logs:
```sh
docker logs <container name/id>
```
