from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers import usuario_controller
from models.usuario_model import Usuario

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/cadastro")
def cadastrar_usuario(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    whatsapp: str = Form(...),
    senha: str = Form(...),
    rua: str = Form(...),
    numero: str = Form(...),
    complemento: str = Form(None),
    cep: str = Form(...),
    ponto: str = Form(None)
):
    usuario = Usuario(
        nome=nome,
        email=email,
        whatsapp=whatsapp,
        senha=senha,
        rua=rua,
        numero=numero,
        complemento=complemento,
        cep=cep,
        ponto_referencia=ponto
    )
    usuario_controller.cadastrar_usuario(usuario)
    return RedirectResponse(url="/login", status_code=303)


@router.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)
):
    usuario = usuario_controller.autenticar_usuario(email, senha)
    if usuario:
        return RedirectResponse(url="/meus-pedidos", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "mensagem_erro": "email ou senha invalidos"
        },status_code=200)


@router.get("/meus-pedidos", response_class=HTMLResponse)
def meus_pedidos(request: Request):
    return templates.TemplateResponse("pedidos.html", {"request": request})


@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
def cadastro_page(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


@router.get("/pedidos", response_class=HTMLResponse)
def pedidos_page(request: Request):
    return templates.TemplateResponse("pedidos.html", {"request": request})


