import os
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI()

with open("data/test.json") as file:
	data = json.load(file)


@app.get("/")
def fetch_all():
	return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
