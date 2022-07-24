import string
from typing import List
from app.api.service_gophish import api
from app.api.models import GophishUser, GophishGroup 
from gophish.models import *


newGroup = List(GophishGroup)
def prepareUserForGroup(first_name : string, last_name : string, email: string, position: string):
    return newGroup.append(GophishUser(first_name, last_name, email, position))



def createGroup(name: string, targets: List(GophishGroup)):



    return

def sendCampaign():
    groups = [Group(name='Existing Group')]
    page = Page(name='Existing Page')
    template = Template(name='Existing Template')
    smtp = SMTP(name='Existing Profile')
    url = 'http://phishing_server'
    campaign = Campaign(
        name='Example Campaign', groups=groups, page=page,
        template=template, smtp=smtp)

    campaign = api.campaigns.post(campaign)
    print campaign.id

    return

def createTemplate():

    template = Template(name='Test Template',
    html='<html><body>Click <a href="{{.URL}}">here</a></body></html>')

    template = api.templates.post(template)
    print template.id

    return

def sendProfile():
    smtp = SMTP(name='Test SMTP')
    smtp.host = "localhost:25"
    smtp.from_address = "John Doe <johndoe@example.com>"
    smtp.interface_type = "SMTP"
    smtp.ignore_cert_errors = True

    smtp = api.smtp.post(smtp)
    print smtp.id
    return
