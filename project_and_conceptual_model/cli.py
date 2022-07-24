import sys
import datetime
import requests
from time import gmtime, strftime
  
  
def help():
    usage = """Usage :-
$ ./todo createCategory "category_name"                                                 # Create new category
$ ./todo listCategories                                                                 # List all categories
$ ./todo createSubCategory "subcategory_name;category_id"                               # Create new subcategory
$ ./todo listSubCategories                                                              # List all subcategories
$ ./todo createTemplate "name;templatestring;categoryid;subcategoryid"                  # Create new template
$ ./todo listTemplates                                                                  # List all templates
$ ./todo sendCampaign "templateid"                                                      # Send new Campaign
$ ./todo listCampaigns                                                                  # List all campaigns
$ ./todo help                                                                           # Show usage"""
    sys.stdout.buffer.write(usage.encode('utf8'))
  
def createCategory(s):
    params = s.split(";")
    category_name = params[0]
    response = requests.post('http://localhost:8080/api/v1/category', data = {'categoy_name':category_name})
    return response

def listCategories():
    response = requests.get('http://localhost:8080/api/v1/category')
    print(response)
    return response

def createSubCategory(s):
    params = s.split(";")
    subcategory_name = params[0]
    category_id = params[1]
    response = requests.post('http://localhost:8080/api/v1/subcategory', data = {'subcategory_name':subcategory_name,'category_id':category_id}
    return response

def listSubCategories():
    response = requests.get('http://localhost:8080/api/v1/subcategory')
    print(response)
    return response

def createTemplate(s):
    params = s.split(";")
    template_name = params[0]
    template_string = params[1]
    category_id = params[2]
    subcategory_id = params[3]
    response = requests.post('http://localhost:8080/api/v1/template', data = {'template_name':template_name, "template_string":template_string, "categoryid":category_id, "subcategoryid": subcategory_id})
    return response

def listTemplates():
    response = requests.get('http://localhost:8080/api/v1/template')
    print(response)
    return response

def sendCampaign(s):
    params = s.split(";")
    templateid = params[0]
    period = strftime("%Y-%m-%d", gmtime())
    response = requests.post('http://localhost:8080/api/v1/campaign', data = {'templateid': templateid, 'period': period}
    return response

def listCampaigns():
    response = requests.get('http://localhost:8080/api/v1/campaign')
    print(response)
    return response
  
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
        
        if(args[1] == 'createCategory' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing arguments string. Nothing will be done".encode('utf8'))
  
        elif(args[1] == 'createSubCategory' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing arguments string. Nothing will be done".encode('utf8'))
  
        elif(args[1] == 'createTemplate' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing arguments string. Nothing will be done".encode('utf8'))

        elif(args[1] == 'sendCampaign' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing arguments string. Nothing will be done".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
  
    except Exception as e:
  
    usage = """Usage :-
$ ./todo createCategory "category_name"                                                 # Create new category
$ ./todo listCategories                                                                 # List all categories
$ ./todo createSubCategory "subcategory_name;category_id"                               # Create new subcategory
$ ./todo listSubCategories                                                              # List all subcategories
$ ./todo createTemplate "name;templatestring;categoryid;subcategoryid"                  # Create new template
$ ./todo listTemplates                                                                  # List all templates
$ ./todo sendCampaign "templateid"                                                      # Send new Campaign
$ ./todo listCampaigns                                                                  # List all campaigns
$ ./todo help                                                                           # Show usage"""
        sys.stdout.buffer.write(usage.encode('utf8'))