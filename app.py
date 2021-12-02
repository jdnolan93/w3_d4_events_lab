from flask import Flask

app = Flash(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)