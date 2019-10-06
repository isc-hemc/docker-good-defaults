"""Celery module.

Attributes
----------
app : Celery
    Instance used as the entry-point for Celery tasks.

"""


from celery import Celery

app = Celery("async_tasks", include=["async_tasks.tasks"])

app.config_from_object("async_tasks.celeryconfig")
