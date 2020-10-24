#Flask
from flask import request

from helpers import handler_response

from app import Directory

directory = Directory()

def routes(app):

    @app.route('/api', methods = ['POST'])
    def api_content():
        values = request.values
        path_directory = values.get('path')
        sort_by = 'file_size' if not values.get('order') else values.get('order')
        sort_reverse = True if values.get('reverse_order') == 'True' else False
        return directory.data(path_directory, sort_by, sort_reverse, app)
