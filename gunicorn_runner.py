import os
import subprocess
import sys

__author__ = 'Imam Hossain Roni'
__email__ = "imamhossainroni95@gmail.com"
__status__ = "Development"


class GunicornRunner:
    """
        Utility class for running Gunicorn server from a virtual environment.

        This class helps find the location of the Gunicorn executable within the
        virtual environment and run it with the specified parameters.

        Usage:
        ```
        gunicorn_runner = GunicornRunner()
        gunicorn_runner.run_gunicorn()
        ```

        Attributes:
            venv_path (str): The path to the virtual environment.
        """

    def __init__(self):
        self.venv_path = self.get_venv_path()

    @staticmethod
    def get_venv_path():
        base_prefix = getattr(sys, 'base_prefix', None)
        real_prefix = getattr(sys, 'real_prefix', None)

        if real_prefix and base_prefix != real_prefix:
            venv_path = real_prefix
        else:
            venv_path = sys.prefix

        return venv_path

    def get_gunicorn_location(self):
        gunicorn_location = os.path.join(self.venv_path, "bin", "gunicorn")
        return gunicorn_location if os.path.exists(gunicorn_location) else None

    def run_gunicorn(self):
        gunicorn_location = self.get_gunicorn_location()

        try:
            if gunicorn_location:
                command = f"{gunicorn_location} -w 4 -b localhost:8000  app:app --reload"
                subprocess.call(command, shell=True)
            else:
                print("\033[91mGunicorn executable not found in the virtual environment.\033[0m")

        except KeyboardInterrupt:
            print("Gunicorn process terminated.")
            sys.exit(0)

    def get_log(self):
        # Will implement log retrieval logic here if needed in future
        pass


if __name__ == "__main__":
    gunicorn_runner = GunicornRunner()
    gunicorn_runner.run_gunicorn()
