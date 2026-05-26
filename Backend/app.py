from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "ok": True,
        "mensaje": "Backend de test funcionando"
    }


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)


@app.get("/ping")
def ping():
    return {
        "ok": True,
        "mensaje": "Backend funcionando"
    }


@app.get("/api/ping")
def api_ping():
    return ping()
