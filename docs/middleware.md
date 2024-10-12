### Creating Custom Middleware
To create custom middleware in PyKite, follow these steps:

1. Create a Middleware Class: Define a class that extends `BaseMiddleware` and implement the `process_request` and `process_response` methods.
```python
class CustomMiddleWare(BaseMiddleware):
    def process_request(self, request, response):
        print("Middleware1: Before request processing")
        return request, response

    def process_response(self, request, response):
        print("Middleware1: After request processing")
        response.text = "Modified response"
        return response
```
2. Register the Middleware: Add the middleware to the application using the below instructions.
```python
app = PyKite(
    debug=True,
    middlewares=[CustomMiddleWare]
     )
```
### Middleware Execution Flow
You can register multiple middleware components. They will be executed in the order they are registered:
* Pre-Processing (`process_request`): Executed before the request reaches the route handler.
* Post-Processing (`process_response`): Executed after the route handler generates a response.