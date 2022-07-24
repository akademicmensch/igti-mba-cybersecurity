from array import array
import string
from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts_id: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None

class CategoryCreated:
    def __init__(self, response):
        self.response: string

class CreateCategory:
    def __init__(self, category_name):
        self.categoy_name: string

class SubCategoryCreated:
    def __init__(self, response):
        self.response: string

class CreateSubCategory:
    def __init__(self, subcategory_name, categoryid):
        self.categoy_name: string
        self.categoryid: int

class CategoryList:
    def __init__(self):
        self.id: int
        self.name: string

class SubCategoryList:
    def __init__(self):
        self.id: int
        self.name: string

class TemplateCreated:
    def __init__(self, response):
        self.response: string

class CampaignCreated:
    def __init__(self, response):
        self.response: string

class CreateTemplate:
    def __init__(self, template_name, template_string, categoryid, subcategoryid):
        self.template_name: string
        self.template_string: string
        self.categoryid: int
        self.subcategoryid: int

class CreateCampaign:
    def __init__(self, campaign_name, templateid, period):
        self.campaign_name: string
        self.templateid: int
        self.period: int

class TemplateList:
    def __init__(self):
        self.id: int
        self.template_name: string
        self.template_string: string
        self.categoryid: int
        self.subcategoryid: int

class CampaingList:
    def __init__(self):
        self.id: int
        self.templateid: int
        self.period: int

class GophishUser:
    def __init__(self, first_name, last_name, email, position):
        id: int
        self.first_name: string
        self.last_name: string
        self.email: string
        self.position: string

class GophishGroup:
    def __init__(self, group_name, targets):
        self.group_name: string
        self.targets: List(GophishUser)