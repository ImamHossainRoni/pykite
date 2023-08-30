import sys
from webob import Request, Response
from parse import parse
from werkzeug.serving import run_simple


class PyKite:
    def __init__(self, debug=False):
        self.routes = {}
        self.debug = debug

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response, *args, **kwargs):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def run(self, host='localhost', port=8000):
        try:
            print(f'Serving on http://{host}:{port}')
            run_simple(host, port, self, use_reloader=True)

        except KeyboardInterrupt:
            print("\033[91mServing process terminated.\033[0m")
            sys.exit(0)

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parsed_result = parse(path, request_path)
            if parsed_result is not None:
                return handler, parsed_result.named
        return None, None

    def handle_request(self, request):
        response = Response()

        # Check if debug flag is True and print some debug information
        if self.debug:
            print(f"Request received: {request.method} {request.path}")

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None and kwargs is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response
