from getopt import gnu_getopt
import string
from typing import List
from app.api.service_gophish import api
from app.api.models import GophishUser, GophishGroup
from gophish.models import *


newGroup = List(GophishGroup)
defaultgroups = []
group = Group(name = 'Empresa a ser testada')
defaultgroups.append(group)
def prepareUserForGroup(first_name : string, last_name : string, email: string, position: string):
    return newGroup.append(GophishUser(first_name, last_name, email, position))

def createGroup(name: string, targets: List(GophishGroup)):
    group = Group(name='Empresa a ser testada', targets=targets)
    group = api.groups.post(group)
    return

def sendCampaign(temp: Template, camp: Campaign):
    groups = defaultgroups
    template = temp
    smtp = SMTP(name='Empresa a ser testada')
    url = 'http://phishing_server'
    campaign = Campaign(
        name=camp.name, groups=groups,
        template=temp, smtp=smtp)

    campaign = api.campaigns.post(campaign)

    return

def createTemplate(template_name: string, html_string_template: string):
    template = Template(name=template_name,
    html=html_string_template)

    template = api.templates.post(template)
    return

def sendProfile():
    smtp = SMTP(name='Test SMTP')
    smtp.host = "localhost:25"
    smtp.from_address = "John Doe <johndoe@example.com>"
    smtp.interface_type = "SMTP"
    smtp.ignore_cert_errors = True

    smtp = api.smtp.post(smtp)
    return
