"""Main module of the server application.

In development, if you execute this file it will run the flask default develop-
er server to launch the service, if it's in production the wsgi will search
for the app variable that it's imported from `entrypoint` and will launch the
service.

"""


from app import app

if __name__ == "__main__":
    app.run()
