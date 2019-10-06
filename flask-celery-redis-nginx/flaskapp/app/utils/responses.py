"""Responses.

Provides a custom response class to avoid hard-coding the HTTP status, message,
body, headers, etc.

"""

import json
from typing import Dict, Optional

from flask import Response


class CustomResponse:
    """Custom HTTP Response Helper."""

    def __init__(
        self,
        message: Optional[str] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
    ):
        """Constructor.

        Attributes
        ----------
        message : str, optional
            Custom message.
        data : Dict, optional
            Payload to attach to the response.
        headers : Dict, optional
            HTTP headers.

        """
        self.message = message
        self.data = data
        self.headers = headers

    def success(self, status_code: int = 200) -> Response:
        """Success HTTP Response.

        Parameters
        ----------
        status_code : int
            HTTP success status code.

        Returns
        -------
        HttpResponse

        Raises
        ------
        ValueError
            If status code is lower than 200 or bigger than 226.

        """
        if status_code < 200 or status_code > 226:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            json.dumps({"message": self.message, "data": self.data}),
            status=status_code,
            headers=self.headers,
        )

    def error(self, status_code: int = 400) -> Response:
        """Error HTTP Response.

        Parameters
        ----------
        status_code : int
            HTTP error status code.

        Returns
        -------
        HttpResponse

        Raises
        ------
        ValueError
            If status code is lower than 400 or bigger than 521.

        """
        if status_code < 400 or status_code > 521:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            json.dumps({"message": self.message, "errors": self.data}),
            status=status_code,
            headers=self.headers,
        )
