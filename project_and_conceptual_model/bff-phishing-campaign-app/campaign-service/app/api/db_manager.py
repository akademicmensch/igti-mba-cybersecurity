from app.api.models import CreateSubCategory, CreateCategory, CreateTemplate
from app.api.db import category, subcategory, template, campaign, database


async def create_category(payload: CreateCategory):
    query = category.insert().values(**payload.dict())


async def create_subcategory(payload: CreateSubCategory):
    query = subcategory.insert().values(**payload.dict())


async def list_categories():
    query = category.select()
    return await database.fetch_all(query=query)


async def list_subcategories():
    query = category.select()
    return await subcategory.fetch_all(query=query)


async def create_template(payload: CreateTemplate):
    query = template.insert().values(**payload.dict())


async def list_template():
    query = template.select()
    return await database.fetch_all(query=query)


async def create_camapign(payload: CreateTemplate):
    query = campaign.insert().values(**payload.dict())


async def list_campaign():
    query = campaign.select()
    return await database.fetch_all(query=query)