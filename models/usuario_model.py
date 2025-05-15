import hashlib
from database.db import conectar

class Usuario:
    def __init__(self, nome, email, whatsapp, senha, rua, numero, cep, ponto_referencia, complemento=None,id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.whatsapp = whatsapp
        self.senha = senha
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.ponto_referencia = ponto_referencia

    def criptografar_senha(self):
        return hashlib.sha256(self.senha.encode()).hexdigest()

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO usuarios
                (nome, email, whatsapp, senha, rua, numero, complemento, cep, ponto_referencia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.nome,
                self.email,
                self.whatsapp,
                self.criptografar_senha(),
                self.rua,
                self.numero,
                self.complemento,
                self.cep,
                self.ponto_referencia
            )
            cursor.execute(sql, valores)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def autenticar(email: str, senha: str):
        conn = conectar()
        cursor = conn.cursor()
        try:
            senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
            cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha_criptografada))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()
