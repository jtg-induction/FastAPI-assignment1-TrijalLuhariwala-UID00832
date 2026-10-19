from fastapi import FastAPI, status

from typing import Optional

from app.core.config import settings
from app.db.config import init_db

app = FastAPI(title=settings.PROJECT_NAME)

init_db(app)

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check(mssg : Optional[str] = None):
    return {
        "status": "healthy",
        "mssg": mssg
        }
