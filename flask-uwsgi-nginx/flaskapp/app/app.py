"""Flask server.

Simple flask application with a single endpoint.

Attributes
----------
app : Flask
    Flask instance to run our service.

"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """Root endpoint.

    Returns
    -------
    HttpResponse

    """
    return "<h1>Hello, world!</h1>"
