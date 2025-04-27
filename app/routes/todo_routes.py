from fastapi import APIRouter, Depends, HTTPException, status
from ..models.todo_models import Text_model, Text_model_Resquest
from ..services.todo_service import TodoService

router = APIRouter()

todoService = TodoService()


@router.get("/health")
async def health_check():
    return {"status": status.HTTP_200_OK, "message": "API is running"}

@router.get("/")
async def hello():
    return {"status": status.HTTP_200_OK, "message": "Hello World"}   
     
     
@router.post("/todo" , response_model=dict)
async def create_todo(todo: Text_model):
    
    return todoService.create_todo(todo) 