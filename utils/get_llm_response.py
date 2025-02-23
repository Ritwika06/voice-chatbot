from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM  

def get_mistral_llm_response(trans):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. You only give short answers to all questions. \
              USE IN ENGLISH LANGUAGE ONLY"),
            ("human", "{input}"),
        ]
    )

    model = OllamaLLM(model="mistral")
    
    chain = prompt | model
    response = chain.invoke(input=trans)
    
    return response