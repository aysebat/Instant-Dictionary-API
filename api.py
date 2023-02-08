import justpy as jp
import definition
import json


class Api:
    """Handles requests at /api?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage(classes="font-mono")
        #getting the word from the URL
        word = req.query_params.get('w')

        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }
        #just pass the text what the request get
        wp.html = json.dumps(response)
        return wp

