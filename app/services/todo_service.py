from ..models.todo_models import Text_model
from ..core.database import MongoDB
from datetime import datetime as Date
from fastapi import HTTPException, status

class TodoService:
    
    db = MongoDB.get_db()
    
    @classmethod
    def create_todo( cls, model : Text_model ):
        
        collection = cls.db["datas"]
        
        todo = {
            "text": model.text,
            "created_at": Date.utcnow(),
            "updated_at": Date.utcnow(),
            "done" : False
        }
        
        result = collection.insert_one(todo)
        
        if not result.acknowledged:
            raise HTTPException( status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create todo" )
    
        data = {
            "id": str(result.inserted_id),
            "text": todo["text"],
            "created_at": todo["created_at"],
            "updated_at": todo["updated_at"],
            "done" : todo["done"]
        }
        
        return data 
        
        
         
        
        

    def get_todo(self, todo_id):
        return self.todo_repository.get_todo(todo_id)

    def update_todo(self, todo_id, title=None, description=None):
        return self.todo_repository.update_todo(todo_id, title, description)

    def delete_todo(self, todo_id):
        return self.todo_repository.delete_todo(todo_id)