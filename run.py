import os
import subprocess
import sys


def get_venv_path():
    base_prefix = getattr(sys, 'base_prefix', None)
    real_prefix = getattr(sys, 'real_prefix', None)

    if real_prefix and base_prefix != real_prefix:
        # Using virtualenv or venv
        venv_path = real_prefix
    else:
        # Running without virtualenv or venv
        venv_path = sys.prefix

    return venv_path


def get_gunicorn_location(venv_path):
    gunicorn_location = os.path.join(venv_path, "bin", "gunicorn")
    return gunicorn_location if os.path.exists(gunicorn_location) else None


def main():
    venv_path = get_venv_path()
    gunicorn_location = get_gunicorn_location(venv_path)
    try:

        if gunicorn_location:
            command = f"{gunicorn_location} app:app --reload"
            subprocess.call(command, shell=True)
        else:
            print("\033[91mGunicorn executable not found in the virtual environment.\033[0m")
    except KeyboardInterrupt:
        print("Gunicorn process terminated.")
        sys.exit(0)  # Exit gracefully without showing traceback


if __name__ == "__main__":
    main()
