#! python
# -*- coding: utf-8 -*-

"""
Class: BaseMiddleware (base.py)
Author: Imam Hossain Roni
Created: October 12, 2024

Description: This class provides the foundation for building custom middleware in a Python web framework.
             It defines an abstract base class (ABC) named `BaseMiddleware` that enforces a standard structure
             for request and response processing within middleware implementations. This promotes code consistency
             and reusability.

             - Subclasses of `BaseMiddleware` must implement the abstract methods `process_request` and
               `process_response` to define their specific middleware logic.
             - The `__call__` method provides a default flow for handling requests and responses,
               allowing middleware subclasses to modify or extend this behavior.
"""

from abc import ABC, abstractmethod
from typing import Optional, Callable, Tuple, Any


class BaseMiddleware(ABC):
    """
       An abstract base class that serves as a template for building middleware in a web application framework.

       The `BaseMiddleware` class provides the structure for creating middleware components that can process
       requests and responses. Middleware sits between the request and response cycle, allowing for pre- and
       post-processing of requests and responses. Subclasses must implement the `process_request` and
       `process_response` methods.

       Args:
           app (Callable, optional): The next layer of the application to call after processing the request
           and response. This allows chaining of multiple middleware layers.

       Attributes:
           app (Callable): The next callable application layer to pass control to after this middleware.
    """

    def __init__(self, app: Optional[Callable] = None):
        self.app = app

    def __call__(self, request: Any, response: Any) -> Tuple[Any, Any]:
        """
        The call method of the middleware.
        Args:
            request: The incoming request object.
            response: The outgoing response object.
        Returns:
            A tuple containing the processed request and response objects.
        """
        request, response = self.process_request(request, response)
        response = self.process_response(request, response)
        return request, response

    @abstractmethod
    def process_request(self, request: Any, response: Any) -> Tuple[Any, Any]:
        """
        Processes the request before it reaches the view.
        Args:
            request: The incoming request object.
            response: The outgoing response object.
        Returns:
            A tuple containing the processed request and response objects.
        """
        pass

    @abstractmethod
    def process_response(self, request: Any, response: Any) -> Any:
        """
        Processes the response after the view has finished execution.
        Args:
            request: The incoming request object.
            response: The outgoing response object.
        Returns:
            The processed response object.
        """
        pass
