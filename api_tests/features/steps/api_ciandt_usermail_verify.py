import requests
import re
import json

@then(u'the users mails must be valid')
def step_impl(context):
    payload = {'id': '1'}
    regex = '^[a-z]([w-]*[a-z]|[w-.]*[a-z]{2,}|[a-z])*@[a-z]([w-]*[a-z]|[w-.]*[a-z]{2,}|[a-z]){4,}?.[a-z]{2,}$'
    call = requests.get('https://jsonplaceholder.typicode.com/users/1', params=payload)
    
    call
    
    response = call.json()
    print(response)
    
    if response.email != None:
        
        assert(re.match(regex, response.email))
