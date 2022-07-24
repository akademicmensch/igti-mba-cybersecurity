from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import CategoryCreated, CreateCategory, SubCategoryCreated, CreateSubCategory, CategoryList, SubCategoryList, CreateTemplate, TemplateCreated, CreateCampaign, CampaignCreated, TemplateList, CampaingList
from app.api import db_manager
from app.api import service_gophish

campaigns = APIRouter()


@campaigns.post('/category', response_model=CategoryCreated, status_code=201)
async def create_category(payload: CreateCategory):
    categoy = await db_manager.create_category(payload)
    return CategoryCreated('created')

@campaigns.post('/subcategory', response_model=SubCategoryCreated, status_code=201)
async def create_category(payload: CreateSubCategory):
    categoy = await db_manager.create_subcategory(payload)
    return SubCategoryCreated('created')

@campaigns.get('/category', response_model=List[CategoryList], status_code=200)
async def list_categories():
    categories = await db_manager.list_categories()
    return categories

@campaigns.get('/subcategory', response_model=List[SubCategoryList], status_code=200)
async def create_category():
    subcategories = await db_manager.list_subcategories()
    return subcategories

@campaigns.post('/template', response_model=TemplateCreated, status_code=201)
async def create_template(payload: CreateTemplate):
    template = await db_manager.create_template(payload)

    service_gophish.createTemplate(payload.template_name, payload.template_string)

    return TemplateCreated('created')

@campaigns.get('/template', response_model=List[TemplateList], status_code=200)
async def list_template():
    templates = await db_manager.list_template()
    return templates


@campaigns.post('/', response_model=CampaignCreated, status_code=201)
async def create_campaign(payload: CreateCampaign):
    subcategories = await db_manager.create_campaign()

    service_gophish.sendCampaign(payload.campaign_name, payload.templateid)

    return TemplateCreated('created')

@campaigns.get('/', response_model=List[CampaingList], status_code=200)
async def list_campaign():
    campaigns = await db_manager.list_campaign()
    return campaigns


@movies.put('/{id}/', response_model=MovieOut)
async def update_movie(id: int, payload: MovieUpdate):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if 'casts_id' in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await db_manager.update_movie(id, updated_movie)

@movies.delete('/{id}/', response_model=None)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)
