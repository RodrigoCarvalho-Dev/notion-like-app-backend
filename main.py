from fastapi import FastAPI
from app.core.database import MongoDB
from app.routes import todo_routes
from contextlib import asynccontextmanager
from dotenv import load_dotenv


app = FastAPI()

load_dotenv()

@asynccontextmanager
async def lifespan( app : FastAPI ):
    
    MONGODB = MongoDB()
    
    print("Iniciando o banco de dados...")
    await MONGODB.init_db()
    print("Banco de dados iniciado.")
    yield
    await MONGODB.close_db()
    print("Banco de dados fechado.")

print("Iniciando o FastAPI")

app = FastAPI( lifespan=lifespan )

app.include_router(
    router= todo_routes.router   ,  # Substitua pelo seu roteador real
    prefix="/api/v1",
)

