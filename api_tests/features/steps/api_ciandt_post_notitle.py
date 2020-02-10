import requests

@then(u'post without title')
def step_impl(context):
    url = 'https://jsonplaceholder.typicode.com/users'
    data = {'id': '1', 'name': 'Allan Barroso', 'username': 'Abarroso', 'email': 'allan.barroso@outlook.com',}
    
    requests.post(url, data=data)
