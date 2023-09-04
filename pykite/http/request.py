#! python
# -*- coding: utf-8 -*-

"""
Module: request.py
Author: Imam Hossain Roni
Created: September 05, 2023

Description: ''
"""
from urllib.parse import parse_qs
from http.cookies import SimpleCookie

__author__ = 'Imam Hossain Roni'
__email__ = "imamhossainroni95@gmail.com"
__status__ = "Development"


class HttpRequest:
    """
    A basic HTTP request.

    Attributes:
        environ (dict): The WSGI environment dictionary containing request details.
        GET (dict): A dictionary containing query parameters from the request.
        POST (dict): A dictionary containing form data from the request.
        path (str): The requested URL path.
        path_info (str): Additional path information, if available.
        method (str): The HTTP request method (e.g., GET, POST).
        content_type (str): The content type of the request body, if applicable.
        content_params (dict): Parameters related to the request content.

    """

    def __init__(self, environ):
        self.environ = environ
        self.GET = {}
        self.POST = {}

        self.path = ""
        self.path_info = ""
        self.method = None
        self.content_type = None
        self.content_params = None


class Request:
    """
       Represents an HTTP request within the PyKite framework.

       Inherits from HttpRequest.

       Attributes:
           Inherits all attributes from the HttpRequest class.

    """
    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']

        self.headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                header_name = key[5:].replace('_', '-').title()
                self.headers[header_name] = value

        self.query_params = parse_qs(environ.get('QUERY_STRING', ''))

        content_length = int(environ.get('CONTENT_LENGTH', 0))
        if content_length > 0:
            self.body = environ['wsgi.input'].read(content_length)
        else:
            self.body = b''

        self.cookies = SimpleCookie()
        cookie_header = self.headers.get('Cookie', '')
        self.cookies.load(cookie_header)
