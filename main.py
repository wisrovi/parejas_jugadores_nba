#pip install jinja2

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


class Value(BaseModel):
    value: int


class Rta_base(BaseModel):
    parejas: tuple


class Rta(BaseModel):
    data: list[Rta_base]


@app.get("/", response_class=HTMLResponse)
async def create_item():
    return templates.TemplateResponse("response.html", {})


@app.post("/response")
async def root(value: Value):
    datos = Rta_base(parejas=("queso", "pan"))
    listado_datos = [datos]
    rta = Rta(data=listado_datos)
    return rta

