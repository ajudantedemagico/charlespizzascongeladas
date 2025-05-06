#from database import db  # ou o caminho correto até seu db.py

#def testar_conexao():
 #   try:
        #conexao = db.conectar()
        #cursor = conexao.cursor()
        #cursor.execute("SELECT 1")
        #resultado = cursor.fetchone()
        #print("✅ Conexão com o banco funcionando:", resultado)
        #cursor.close()
        #conexao.close()
    #except Exception as e:
        #print("❌ Erro ao conectar com o banco:", e)

# Executa o teste ao iniciar
#testar_conexao()

from fastapi import FastAPI
from routes.usuario_routes import router as usuario_routes
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

app.include_router(usuario_routes)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)