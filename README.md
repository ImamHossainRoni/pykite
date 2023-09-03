# PyKite: A research and development initiative for crafting a Python-centric micro framework.
---

[//]: # (![Pykite, the Python framework]&#40;./extras/yellow-kite.png&#41;)
<img src="./extras/yellow-kite.png" height="500">

---

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

app = PyKite(debug=True)

@app.route('/')
def index(request, response):
    response.text = 'Hello, PyKite!'
    return response

if __name__ == '__main__':
    app.run()

```
3. Access your application in a web browser at http://localhost:8000.





