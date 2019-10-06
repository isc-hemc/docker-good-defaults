"""Celery tasks module."""


from async_tasks.celery import app


@app.task(name="reverse")
def reverse(string: str) -> str:
    """Reverse.

    Parameters
    ----------
    string : str
        String to reverse.

    Returns
    -------
    str
        Reversed string.

    """
    return string[::-1]
