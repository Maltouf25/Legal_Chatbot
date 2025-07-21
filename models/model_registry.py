from .Embedding_Model import Embedding_Model


model_registry = {
    "Embedding_Model" :lambda :Embedding_Model(),
    "GPT_Model":lambda :GPT_Model()
    # "Openai_api_Model":lambda :Openai_api_Model(),
    # "Ollama_model":lambda :Ollama_model()
}