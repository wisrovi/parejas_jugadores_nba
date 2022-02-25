# pip install jinja2
# pip install "uvicorn[standard]"
# pip install python-multipart

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from lib.BusquedaHeuristica import BusquedaHeuristica

templates = Jinja2Templates(directory="templates")

app = FastAPI()


class Value(BaseModel):
    value: int


class Rta_base(BaseModel):
    parejas: tuple


class Rta(BaseModel):
    data: list[Rta_base]


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
async def form_post(request: Request):
    result = "Type a number"
    data = []
    inicial = 139
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'data': data, 'inicial': inicial})


@app.post("/form")
async def form_post(request: Request, num: int = Form(...)):
    rp = BusquedaHeuristica("https://mach-eight.uc.r.appspot.com/")
    rp.search(num)
    rta = rp.solve(False)
    if rta is not None:
        data = rta
        result = ""
    else:
        data = []
        result = "No se encontraron coincidencias"

    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'data': data, 'inicial': num})

