from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from src.users.router import user_router
from src.products.router import router as product_router
from src.models import Base
from src.database import db_helper
from src.auth.router import router as demo_auth_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#   yield


app = FastAPI(docs_url="/docs", openapi_url="/openapi.json")  # , lifespan=lifespan)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(router=demo_auth_router)


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: str | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__name__":
    import uvicorn

    uvicorn.run("src.main:app", reload=True, port=8005)
