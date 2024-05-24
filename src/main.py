from fastapi import FastAPI

app = FastAPI()


if __name__ == "__name__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
