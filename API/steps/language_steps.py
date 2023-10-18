import requests
from behave import *
from hamcrest import assert_that, equal_to

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"


@when('a GET request is sent with correct parameters')
def get_all_languages(context):
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.get(url, headers=headers)
    context.response_status = context.response.status_code


@then('all languages available to translate')
def verify_all_languages(context):
    response_json = context.response.json()
    count = len(response_json["data"]["languages"])
    expected_count = 136
    assert_that(count, equal_to(expected_count))


@when('a GET request is sent without key')
def get_without_key(context):
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.get(url, headers=headers)
    context.response_status = context.response.status_code


@when('a GET request is sent with more parameters than expected on headers')
def get_with_more_parameters_than_expected(context):
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X": "whats happen?"
    }

    context.response = requests.get(url, headers=headers)
    context.response_status = context.response.status_code


@then('the response status should be 429')
def response_status_429(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(429))



@when('a GET request is sent optional parameters field')
def get_with_more_parameters_than_expected(context):
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X": "whats happen?"
    }
    params = {
        "target": "fr",
        "model": "nmt"
    }

    context.response = requests.get(url, headers=headers, params=params)
    context.response_status = context.response.status_code