from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

fastapi_app = FastAPI(
    title= "ml_turnover_serivce.",
    description= "turnover recommendations for HR department.",
    swagger_ui_parameters= {"docExpansion": "None"}
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["GET", "POST"],
    allow_headers = ["*"]
)


@fastapi_app.get("/", status_code= 200)
def read_root():
    return {"Service": "OK"}


app = fastapi_app