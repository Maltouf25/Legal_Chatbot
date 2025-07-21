from abc import ABC , abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def answer(self,user_query:str) -> str :
        pass