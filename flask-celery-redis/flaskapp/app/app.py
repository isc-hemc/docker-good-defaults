"""Flask server.

Simple flask application with three endpoints.

Attributes
----------
flaskapp : Flask
    Flask instance to run our service.

"""


from celery.result import AsyncResult
from flask import Flask

from async_tasks.celery import app
from async_tasks.celeryconfig import broker_url, result_backend
from async_tasks.tasks import reverse
from utils.responses import CustomResponse, Response

flask_app: Flask = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=broker_url, CELERY_RESULT_BACKEND=result_backend
)


@flask_app.route("/async_task_result/<task_id>", methods=["GET"])
def async_task_result(task_id: str) -> Response:
    """Async task result service.

    Parameters
    ----------
    task_id : str
        Taks id to search for its results.

    Returns
    -------
    HttpResponse

    """
    result = AsyncResult(task_id, app=app)
    if result.state == "PENDING":
        return CustomResponse(
            headers={"Content-Type": "application/json"},
            message="I'm a teapot.",
            data={}
        ).error(status_code=418)
    return CustomResponse(
        headers={"Content-Type": "application/json"},
        message="Async task result.",
        data={"id": result.id, "state": result.state, "result": result.get()},
    ).success()


@flask_app.route("/async_task/<string>", methods=["GET"])
def async_task(string: str) -> Response:
    """Async task service.

    Parameters
    ----------
    string : str
        String to reverse with help of celery async task.

    Returns
    -------
    HttpResponse

    """
    task_info = reverse.delay(string=string)
    return CustomResponse(
        headers={"Content-Type": "application/json"},
        message="Processing async task.",
        data={"id": task_info.id, "state": task_info.state}
    ).success()


@flask_app.route("/healthcheck", methods=["GET"])
def heatlhcheck() -> Response:
    """Healthcheck service.

    Returns
    -------
    HttpResponse

    """
    return CustomResponse(
        headers={"Content-Type": "application/json"},
        message="Service working.",
        data={"status": "Ok!"},
    ).success()
