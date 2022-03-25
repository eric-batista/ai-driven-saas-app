# pylint: disable=wrong-import-order
# pylint: disable=wrong-import-position
'''
This module will implement the API routes for GPT-3 model
'''
import sys
from os.path import abspath
sys.path.append(abspath('./../../'))

from fastapi import FastAPI
from src.app.ai_model import generate_branding_snippet, generate_keywords


app = FastAPI()


@app.get('/generate_snippet')
async def generate_branding_snippet_route(prompt: str):
    '''
    >>> This route use the GET method to generate branding snippet
    '''
    snippet = generate_branding_snippet(prompt)

    return {'message': snippet}


@app.get('/generate_keyword')
async def generate_branding_keyword_route(prompt: str):
    '''
    >>> This route use the GET method to generate keywords
    '''
    snippet = generate_keywords(prompt)

    return {'keywords': snippet}
