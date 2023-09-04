# PyKite: A research and development initiative for crafting a Python-centric micro framework.

[//]: # (![Pykite, the Python framework]&#40;./extras/yellow-kite.png&#41;)
![PyKite Icon](https://raw.githubusercontent.com/ImamHossainRoni/pykite/main/extras/yellow-kite.png)

## Features

- **Route Definition:** Define routes using the `@app.route(path)` decorator.

- **HTTP Request Handling:** Create handler functions for each route to process and respond to incoming HTTP requests.

- **Development Server:** Start a development server with a single command, making it easy to test your application locally.

- **Basic Error Handling:** Includes a default 404 response for routes that are not found.


## Installation
To get started with PyKite, follow these steps:
```bash
pip install pykite
```
## Run the application
1. Create a Python script for your web application using PyKite. Define routes and handlers as needed.
2. Run your application using the `run` method:

```python
from pykite import PyKite
from pykite.http.response import Response

# Create a PyKite application
app = PyKite(debug=True)


# Define a route for the '/' path
@app.route('/')
def index(request, response):
    """Respond with a JSON object containing the message "Hello, World!" to all requests to the '/' path."""
    data = {"message": "Hello, World!"}
    response = Response(data=data, status=200)
    return response


@app.route('/hello/{name}')
def hello(request, response, name):
    """ Took a name from the URL and responds with a friendly greeting in JSON."""
    data = {"message": f"Hello, {name}"}
    response = Response(data=data, status=200)
    return response


# Run the application
if __name__ == "__main__":
    app.run()

```
3. Access your application in a web browser at http://localhost:8000.



## License

This project is licensed under the [MIT License](LICENSE).
