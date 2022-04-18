'''
This module will implement the API routes for GPT-3 model
'''
from fastapi import FastAPI, HTTPException
from ai_model import generate_branding_snippet, generate_keywords
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)


MAX_INPUT_LENGTH = 32


def validate_input_lenght(prompt: str):
    '''
    >>>  This function validates the length of prompt input and raise 400 status code
    '''
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f'Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.'
        )


@app.get('/generate_snippet')
async def generate_branding_snippet_route(prompt: str):
    '''
    >>> This route use the GET method to generate branding snippet
    '''
    validate_input_lenght(prompt)
    snippet = generate_branding_snippet(prompt)

    return {'sninppet': snippet, 'keywords': []}


@app.get('/generate_keywords')
async def generate_branding_keyword_route(prompt: str):
    '''
    >>> This route use the GET method to generate keywords
    '''
    validate_input_lenght(prompt)
    keywords = generate_keywords(prompt)

    return {'snippet': None, 'keywords': keywords}

@app.get('/generate_snippet_and_keywords')
async def generate_branding_snippet_and_keyword_route(prompt: str):
    '''
    >>> This route use the GET method to generate branding snippet and keywords
    '''
    validate_input_lenght(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)

    return {'snippet': snippet, 'keywords': keywords}
