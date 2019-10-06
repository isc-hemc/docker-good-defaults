"""Celery configuration.

Celery configuration options for this project.

Attributes
----------
redis_host : str
    IP where redis service is running.
redis_port : str, int
    Redis port that allows connections.
redis_db : str, int
    Redis db to consume.
redis_password : str
    Redis client password.
broker_type : str
    Type of the broker that celery will use.
broker_url : str
    Default broker URL. This must be a URL in the form of:
    `transport://userid:password@hostname:port/virtual_host`.
result_backend : str
    The backend used to store task results (tombstones). Redis example;
    `redis://:password@host:port/db`.
task_serializer : str
    A string identifying the default serialization method to use.
result_serializer : str
    Result serialization format.
accept_content : list
    A white-list of content-types/serializers to allow.
timezone : str
    Configure Celery to use a custom time zone. 
enable_utc : bool
    If enabled dates and times in messages will be converted to use the UTC
    timezone.
"""


import os
from typing import List, Union

redis_host: str = os.environ.get("REDIS_HOST", "127.0.0.1")
redis_port: Union[str, int] = os.environ.get("REDIS_PORT", "6379")
redis_db: Union[str, int] = os.environ.get("REDIS_DB", "0")
redis_bdb: Union[str, int] = os.environ.get("REDIS_BACKEND_DB", "1")
redis_password: str = os.environ.get("REDIS_PASSWORD", "password")

broker_type: str = "redis"
broker_url: str = (
    f"{broker_type}://:{redis_password}@{redis_host}:{redis_port}/{redis_db}"
)
result_backend: str = (
    f"{broker_type}://:{redis_password}@{redis_host}:{redis_port}/{redis_bdb}"
)
accept_content: List[str] = ["json", "application/json"]
result_serializer: str = "json"
task_serializer: str = "json"
enable_utc: bool = True
timezone: str = "UTC"
