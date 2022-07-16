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
