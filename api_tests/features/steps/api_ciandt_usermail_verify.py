import requests
import re

@then(u'the users mails must be valid')
def step_impl(context):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    mail=requests.get('https://jsonplaceholder.typicode.com/users/{email}').text

    if mail != None:
        assert(re.match(regex, mail))
