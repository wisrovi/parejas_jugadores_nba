# pip install jinja2
# pip install "uvicorn[standard]"
# pip install python-multipart
# pip install fastapi
# pip install requests

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from metadata import titulo, description, version, contact, tags_metadata

from lib.BusquedaHeuristica import BusquedaHeuristica

templates = Jinja2Templates(directory="templates")

app = FastAPI(title=titulo,
              description=description,
              version=version,
              contact=contact,
              openapi_tags=tags_metadata)


@app.get("/")
async def form_post(request: Request):
    result = "Type a number"
    data = []
    inicial = 139
    return templates.TemplateResponse('form.html',
                                      context={'request': request, 'result': result, 'data': data, 'inicial': inicial})


@app.post("/")
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

    return templates.TemplateResponse('form.html',
                                      context={'request': request, 'result': result, 'data': data, 'inicial': num})
