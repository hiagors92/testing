import requests
from behave import *
from hamcrest import assert_that, equal_to

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

@when('a POST request is sent with text')
def post_request_sent_text(context):
    payload = {
        "q": "Hello, world!",
        "target": "es",
        "source": "en"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code

@then('the text translated')
def check_text_translated(context):
    response_json = context.response.json()
    translations = response_json.get('data', {}).get('translations', [])
    expected_text = 'Hola, mundo!'
    translated_text = translations[0].get('translatedText')
    assert_that(translated_text, equal_to(expected_text))



@when('a POST request is sent in different languages of english')
def post_request_sent_different_languages(context):
    payload = {
        "q": "Hola, mundo!",
        "target": "pt",
        "source": "es"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code

@when('a POST request is sent without key')
def post_request_sent_without_key(context):
    payload = {
        "q": "Hola, mundo!",
        "target": "pt",
        "source": "es"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code

@when('a POST request is sent with more parameters than expected on headers')
def post_request_sent_with_more_parameters_than_expected(context):
    payload = {
        "q": "Hola, mundo!",
        "target": "pt",
        "source": "es"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X": "whats happen?"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code


@when('a POST request is sent without payload')
def post_request_sent_without_payload(context):
    payload = {

    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code

@when('a POST request is sent with text with special characters')
def send_post_request_with_special_characters(context):
    payload = {
        "q": "H&llo, world!",
        "target": "es",
        "source": "en"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code