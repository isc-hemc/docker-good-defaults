# Flask-Celery-Redis

**Flask-Celery-Redis** is an example project of a Flask API that uses Celery asynchronous task to perform actions in background. Flask API has 3 endpoints:

> /healthcheck - This endpoint only checks the status of the application.

```json
{
    "message": "Service working.",
    "data": {
        "status": "Ok!"
    }
}
```

> /async_task/$(some-string) - This endpoint calls a celery task to reverse $(some-string) in background.

```json
{
    "data": {
        "id": "task_id",
        "state": "SUCCESS"
    },
    "message": "Processing async task."
}
```

> /async_task_result/$(task_id) - Whit the id $(task_id) provided in the previous endpoint you can check the status and the result value of the task.

```json
{
    "message": "Async task result.",
    "data": {
        "id": "task_id",
        "state": "SUCCESS",
        "result": "gnirts-emos"
    }
}
```

Flask and Celery are connected to a Redis server that works as Broker and Result Backend, the configuration of Redis is described below ([Redis](#Redis)). Also, by running this project with Docker, an [NGINX](#NGINX) instance is provided that will redirect all the request to the Flask API.

## Contents

- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Run](#run)
- [Authors](#Authors)

---

## Dependencies

![Python +3.7](https://img.shields.io/badge/python-+3.7-blue.svg)
![Docker](https://img.shields.io/badge/docker-*-blue.svg)
![Redis 5.0](https://img.shields.io/badge/redis-*-red.svg)
![NGINX 1.17.3](https://img.shields.io/badge/nginx-*-green.svg)

---

## Configuration

### Flask and Celery

To run this system it's necessary an **environment file** (**.env**). This file must be in the root of the API and Celery project `/flaskapp/app/.env`.

``` bash
touch .env
```

``` bash
vi .env
```

Then, here's a list of the variables needed with its default value.

#### Conection with the Redis

| Variable             | Value                  |
|----------------------|------------------------|
| REDIS_HOST           | 127.0.0.1              |
| REDIS_PORT           | 6379                   |
| REDIS_DB             | 0                      |
| REDIS_BACKEND_DB     | 0                      |
| REDIS_PASSWORD       | password               |

#### Flask's environment configuration

| Variable             | Value                  |
|----------------------|------------------------|
| FLASK_ENV            | development/production |

### NGINX

The Docker instance of **NGINX** needs an `nginx.conf` file that contains the following custom settings at least:

```bash
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://flask-api-ip:flask-api-port/;
        proxy_set_header Host "localhost";
    }
}

```

You can find this file in `./nginx`, also in this directory is the Dockerfile to create the **NGINX** instance.

### Redis

The Docker instance of **Redis** needs an `redis.conf` file that contains the following custom settings at least:

```bash
pidfile /var/run/redis.pid
requirepass password
databases 16
dir /data
```

You can find this file in `./redis`, also in this directory is the Dockerfile to create the **Redis** instance.

## Run

This system comes with a `docker-compose.yml` file to run it, just open a terminal in this directory and execute:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)
