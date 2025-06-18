import mysql.connector
from mysql.connector import Error
import logging
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

logger = logging.getLogger(__name__)

def get_db_config():
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'database': os.getenv('DB_NAME', 'charles_pizzaria')
    }

def criar_banco_se_nao_existir():
    config = get_db_config()
    try:
        # Conecta sem especificar o banco de dados
        conexao = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
        cursor = conexao.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
        conexao.commit()
        logger.info(f"Banco de dados {config['database']} verificado/criado")
        return True
        
    except Error as e:
        logger.error(f"Erro ao criar banco de dados: {e}")
        return False
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def conectar():
    config = get_db_config()
    try:
        # Primeiro garante que o banco existe
        if not criar_banco_se_nao_existir():
            return None
            
        conexao = mysql.connector.connect(**config)
        return conexao
    except Error as e:
        logger.error(f"Erro ao conectar ao banco: {e}")
        return None

def criar_esquema_pizzaria_se_nao_existir():
    try:
        conexao = conectar()
        if not conexao:
            return False
            
        cursor = conexao.cursor()
        
        # Criação das tabelas
        tabelas = [
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                whatsapp VARCHAR(20) NOT NULL,
                senha VARCHAR(100) NOT NULL,
                rua VARCHAR(100) NOT NULL,
                numero VARCHAR(10) NOT NULL,
                complemento VARCHAR(100),
                cep VARCHAR(11) NOT NULL,
                ponto_referencia VARCHAR(100)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS pedido (
                id_pedido INT AUTO_INCREMENT PRIMARY KEY,
                id_usuario INT NOT NULL,
                data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_entrega DATE,
                status VARCHAR(50) DEFAULT 'Em preparo',
                total DECIMAL(10,2) NOT NULL,
                cupom VARCHAR(50),
                desconto DECIMAL(10,2),
                valor_final DECIMAL(10,2),
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS item_pedido (
                id_item INT AUTO_INCREMENT PRIMARY KEY,
                id_pedido INT NOT NULL,
                sabor VARCHAR(100) NOT NULL,
                tamanho VARCHAR(20) NOT NULL,
                quantidade INT NOT NULL,
                preco_unitario DECIMAL(10,2) NOT NULL,
                subtotal DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE
            )
            """
        ]

                
        for tabela in tabelas:
            cursor.execute(tabela)
        
        conexao.commit()
        logger.info("Esquema do banco verificado/criado com sucesso")
        return True
        
    except Error as e:
        logger.error(f"Erro ao criar esquema: {e}")
        return False
    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()