from main import app

@app.get("/")
async def start_func() -> None:
    return {"message": "Hello world!"}