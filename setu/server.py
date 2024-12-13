


import traceback
from flask import Flask, render_template


app = Flask(__name__)


@app.errorhandler(500)
def internal_server_error(error):
    error_message = traceback.format_stack()
    return render_template('error.html', error_message=error_message), 500