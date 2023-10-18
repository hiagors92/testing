import requests
from behave import *
from hamcrest import assert_that, equal_to


url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"


@given('the translate API endpoint')
def set_api_endpoint(context):
    context.url = url


@when('a POST request is sent with correct parameters')
def send_post_request_with_correct_parameters(context):
    payload = {"q": "Hello"}

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code


@then('the response status should be 200')
def response_status(context):
    assert_that(context.response_status, equal_to(200))


@then('the response status should be 400')
def response_status_400(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(400))


@then('the correct language is detected')
def correct_language_detected(context):
    response_json = context.response.json()
    detected_language = response_json.get('data', {}).get('detections', [])[0][0]['language']
    expected_language = 'en'
    assert_that(detected_language, equal_to(expected_language))


@when('a POST request is sent in different languages to translate')
def send_post_request_with_different_languages(context):
    payload = {"q": "Bom dia"}

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code


@then('the PT language is detected')
def check_pt_language_detected(context):
    response_json = context.response.json()
    detected_language = response_json.get('data', {}).get('detections', [])[0][0]['language']
    expected_language = 'pt'
    assert_that(detected_language, equal_to(expected_language))


@when('a POST request is sent with incorrect header parameters')
def send_post_request_with_incorrect_header_parameters(context):
    payload = {"q": "Hello"}

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/xml",
        "X-RapidAPI-Key": "3333a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code


@then('the response status should be 403')
def response_status_403(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(403))


@when('a POST request is sent without a key in the header')
def send_post_request_without_key(context):
    payload = {"q": "Hello"}

    headers = {
        "content-type": "application/json",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code


@then('the response status should be 401')
def response_status_401(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(401))


@when('a POST request is sent with more parameters than expected in the header')
def send_post_request_with_extra_header_parameters(context):
    payload = {"q": "Hello"}

    headers = {
        "content-type": "application/json",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X": "whats happen?"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code

@then('the response status should be 500')
def response_status_500(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(500))


@when('a POST request is sent without a payload')
def send_post_request_without_payload(context):

    headers = {
        "content-type": "application/json",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
    }

    context.response = requests.post(context.url, data='', headers=headers)
    context.response_status = context.response.status_code

@then('the response status should be 502')
def response_status_502(context):
    context.response_status = context.response.status_code
    assert_that(context.response_status, equal_to(502))

@when('a POST request is sent with text containing special characters')
def send_post_request_with_special_characters(context):
    payload = {"q": "H&llo"}

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "4b79b1e6damsh5a2a5eebd5d07a2p1a7553jsnecf0e4185095",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    context.response = requests.post(context.url, data=payload, headers=headers)
    context.response_status = context.response.status_code



#@when('a lot of POST requests is sent')
#def send_many_post_requests(context):


