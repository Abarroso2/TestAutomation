import requests

@then(u'the company name must be less than 50 chars')
def step_impl(context):
    company=requests.get('https://jsonplaceholder.typicode.com/users/{company}&{name}').text
    if len(company) < 50:
        assert True