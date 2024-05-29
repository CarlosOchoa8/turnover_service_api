from fastapi import APIRouter

from app.endpoints import collaborator_router


api_router = APIRouter()

api_router.include_router(
    router= collaborator_router,
    prefix= "/collaborators",
    tags= ["collaborators"],
    responses= {418: {"Description": "I'm a teapot =)"}}
)
