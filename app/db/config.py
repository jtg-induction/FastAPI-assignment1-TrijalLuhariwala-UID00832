from fastapi import FastAPI
from app.core.config import settings
from tortoise.contrib.fastapi import register_tortoise
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "app.models.users",
                "app.models.orders",
                "app.models.restaurant",
                "aerich.models"
                ],
            "default_connection": "default",
        }
    },
}

def init_db(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
    )