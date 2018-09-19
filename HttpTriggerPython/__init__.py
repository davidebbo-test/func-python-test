import logging
import platform
import os

import azure.functions as func

counter = 0

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    global counter
    counter = counter + 1

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        if 'FOO' not in os.environ:
             os.environ['FOO'] = "NotSet"

        return func.HttpResponse(
            f"Hello {name}! FOO={os.environ['FOO']} host={platform.node()} counter={counter}",
            headers  = {'X-server': platform.node() }
        )
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code = 400
        )
