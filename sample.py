from pykite import PyKite
from pykite.response import Response

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
