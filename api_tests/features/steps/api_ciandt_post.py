import requests

@then(u'post the new name and verify the match')
def step_impl(context):
    url = 'https://jsonplaceholder.typicode.com/users'
    data = {'id': '1', 'name': 'Allan Barroso', 'username': 'Abarroso', 'email': 'allan.barroso@outlook.com',}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(url, data=data, headers=headers)