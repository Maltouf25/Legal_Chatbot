from .base_model import BaseModel


class GPT_Model(BaseModel):
    
    def __init__(self):
        super().__init__()
        


    def answer(self,user_query:str)->str :
        return