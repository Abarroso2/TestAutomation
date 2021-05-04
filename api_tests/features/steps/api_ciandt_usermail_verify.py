import requests
import re
import json

@then(u'the users mails must be valid')
def step_impl(context):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    call = requests.get('https://jsonplaceholder.typicode.com/users/')

    response = json.loads(call.text)

    for user in response:
        
        if (re.match(regex, user['email'])):
            assert True
        else:
            AssertionError()
            print("Invalid user e-mail")
