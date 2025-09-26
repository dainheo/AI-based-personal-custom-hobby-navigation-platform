from fastapi import FastAPI

from auth import models
from auth.database import engine
from auth.routes import router as auth_router


# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Routers
app.include_router(auth_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
