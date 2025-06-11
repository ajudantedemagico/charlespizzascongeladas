# # Adicione no início do main.py
# def testar_conexao():
#     from database.db import conectar
#     conexao = conectar()
#     if conexao:
#         print("✅ Conexão bem-sucedida!")
#         conexao.close()
#     else:
#         print("❌ Falha na conexão")

# # Chame antes de iniciar o FastAPI
# testar_conexao()

from fastapi import FastAPI
from routes.usuario_routes import router as usuario_routes
from routes.admin_routes import router as admin_routes
from routes.pedido_routes import router as pedido_routes
from routes.carrinho_routes import router as carrinho_routes
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from database.db import criar_esquema_pizzaria_se_nao_existir
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="sua_chave_secreta")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

app.include_router(admin_routes)
app.include_router(usuario_routes)
app.include_router(pedido_routes)
app.include_router(carrinho_routes)

@app.on_event("startup")
async def startup_event():
    """Evento executado quando a aplicação inicia"""
    try:
        logger.info("Iniciando aplicação Charles Pizzaria...")
        
        # Criar esquema do banco de dados
        if criar_esquema_pizzaria_se_nao_existir():
            logger.info("Banco de dados verificado/criado com sucesso!")
        else:
            logger.error("Falha ao inicializar o banco de dados!")
        
    except Exception as e:
        logger.critical(f"Erro durante inicialização: {str(e)}")
        raise


if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)