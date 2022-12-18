from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router
from infrastructure.core.config import settings

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
