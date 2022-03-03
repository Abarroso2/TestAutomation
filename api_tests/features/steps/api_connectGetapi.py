import requests
import re

BASE_URL = 'https://jsonplaceholder.typicode.com/'

@given(u'connect with api')
def step_impl(context):
    return requests.get(BASE_URL)


@when(u'request /users')
def step_impl(context):
    usersresponse = requests.get(BASE_URL, 'users')
    

@then(u'the users must be displayed')
def step_impl(context):
    context.usersresponse = requests.get(BASE_URL, 'users')
    
    if context.usersresponse.ok:
        
        assert(context.usersresponse != None)
        return context.usersresponse
    
    else:
        
        return None
    
  
