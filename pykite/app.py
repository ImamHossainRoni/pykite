#! python
# -*- coding: utf-8 -*-

"""
Module: app.py
Author: Imam Hossain Roni
Created: September 01, 2021

Description: 'A research and development initiative for crafting a Python-centric micro framework.'
"""

import sys
from pykite.http import Request, Response
from parse import parse
from werkzeug.serving import run_simple

__author__ = 'Imam Hossain Roni'
__email__ = "imamhossainroni95@gmail.com"
__status__ = "Development"


class PyKite:
    """
    A Python-centric micro-framework for building web applications.

    Args:
        debug (bool, optional): Enable debug mode. Defaults to False.

    Attributes:
        routes (dict): A dictionary to store URL routing.
        debug (bool): Flag for debug mode.

    Methods:
        __init__: Initializes the PyKite instance.
        __call__: Implements the WSGI interface for running the framework.
        route: Decorator for defining routes.
        run: Starts the development server.
        default_response: Generates a default 404 response.
        find_handler: Finds the appropriate route handler.
        handle_request: Handles incoming HTTP requests.
    """

    def __init__(self, debug=False, middlewares=None):
        """
        Initialize the PyKite instance.

        Args:
            debug (bool, optional): Enable debug mode. Defaults to False.
        """
        self.routes = {}
        self.debug = debug
        self.middleware = [middleware_cls(self) for middleware_cls in middlewares] if middlewares else []

    def __call__(self, environ, start_response, *args, **kwargs):
        """
        Implements the WSGI interface for running the framework.

        Args:
            environ (dict): WSGI environment.
            start_response (function): WSGI start_response function.

        Returns:
            list: The response body as a list of byte strings.
        """
        request = Request(environ)
        response = self.handle_request(request)
        for middleware in self.middleware:
            request, response = middleware.process_request(request, response)

        handler, kwargs = self.find_handler(request_path=request.path)
        if handler is not None and kwargs is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        for middleware in reversed(self.middleware):
            response = middleware.process_response(request, response)
        return response(environ, start_response)

    def route(self, path):
        """
        Decorator for defining routes.

        Args:
            path (str): The URL path for the route.

        Returns:
            function: The route handler function.
        """

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def run(self, host='localhost', port=8000):
        """
        Starts the development server.

        Args:
            host (str, optional): The hostname to bind to. Defaults to 'localhost'.
            port (int, optional): The port to bind to. Defaults to 8000.
        """
        try:
            print(f'Serving on http://{host}:{port}')
            run_simple(host, port, self, use_reloader=True)

        except KeyboardInterrupt:
            print("\033[91mServing process terminated.\033[0m")
            sys.exit(0)

    @staticmethod
    def default_response():
        """
        Generates a default 404 response.

        Returns:
            Response: A 404 response object.
        """
        response = Response("Not found.", status=404)
        return response

    def find_handler(self, request_path):
        """
        Finds the appropriate route handler.

        Args:
            request_path (str): The path of the incoming HTTP request.

        Returns:
            tuple: A tuple containing the route handler function and keyword arguments.
        """
        for path, handler in self.routes.items():
            parsed_result = parse(path, request_path)
            if parsed_result is not None:
                return handler, parsed_result.named
        return None, None

    def handle_request(self, request):
        """
        Handles incoming HTTP requests.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: The HTTP response object.
        """
        response = Response()

        # Check if debug flag is True and print some debug information
        if self.debug:
            print(f"Request received: {request.method} {request.path}")

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None and kwargs is not None:
            response = handler(request, response, **kwargs)
        else:
            response = self.default_response()

        return response
