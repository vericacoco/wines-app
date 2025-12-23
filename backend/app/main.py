from fastapi import FastAPI
from app.routes.wines import router as wines_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(wines_router)
