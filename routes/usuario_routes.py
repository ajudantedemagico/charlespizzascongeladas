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
    
    if usuario_controller.autenticar_admin(email, senha):
        request.session["usuario_nome"] = "Administrador"
        return RedirectResponse(url="/admin", status_code=303)

    usuario = usuario_controller.autenticar_usuario(email, senha)
    if usuario:
        nome_usuario = usuario[1]
        request.session["usuario_nome"] = nome_usuario
        return RedirectResponse(url="/meu-carrinho", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "mensagem_erro": "email ou senha invalidos"
        },status_code=200)


@router.get("/meu-carrinho", response_class=HTMLResponse)
def meus_pedidos(request: Request):
    nome_usuario = request.session.get("usuario_nome", "Usuário")
    return templates.TemplateResponse("carrinho.html", {"request": request, "nome_usuario": nome_usuario})


@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/carrinho", response_class=HTMLResponse)
def carrinho_page(request: Request):
    return templates.TemplateResponse("carrinho.html", {"request": request})

@router.get("/pgcliente", response_class=HTMLResponse)
def cliente_page(request: Request):
    return templates.TemplateResponse("pgcliente.html", {"request": request})

@router.get("/admin")
def admin_page_redirect(request: Request):
    nome = request.session.get("usuario_nome", "Desconhecido")
    if nome != "Administrador":
        return RedirectResponse(url="/login", status_code=303)
    return RedirectResponse(url="/admin/usuarios", status_code=303)


