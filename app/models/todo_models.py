from pydantic import BaseModel

class Text_model(BaseModel):     
    text : str = None
    
class Text_model_Resquest(BaseModel):
    text : str  = None


    