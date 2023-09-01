#! python
# -*- coding: utf-8 -*-

"""
Module: response.py
Author: Imam Hossain Roni
Created: September 01, 2023

Description: ''
"""
import json
from webob import Response as WebObResponse

__author__ = 'Imam Hossain Roni'
__email__ = "imamhossainroni95@gmail.com"
__status__ = "Development"


class Response:
    """
     Represents an HTTP response with customizable data and status.

     This class allows you to create HTTP responses with optional data and
     status code. You can provide content in various formats, including plain
     text and JSON.

     Parameters:
         data: The response content (default is None).
         status: The HTTP status code (default is None).

     Example:
         response = Response(data={"message": "Success"}, status=200)
     """

    def __init__(self, data=None, status=None):
        self.data = data
        self.status = status
        self.content_type = "text/plain"

    def __call__(self, environ, start_response):
        if self.data is not None and self.status is not None:

            if isinstance(self.data, dict):
                self.data = json.dumps(self.data)
                self.content_type = "application/json"

            response = WebObResponse(
                body=self.data.encode('utf-8') if isinstance(self.data, str) else self.data,
                content_type=self.content_type,
                status=str(self.status)
            )
        else:
            response = WebObResponse(
                status="500 Internal Server Error"
            )
        return response(environ, start_response)
