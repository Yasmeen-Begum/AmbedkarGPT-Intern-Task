from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain_classic.chains import RetrievalQA

def build_qa_chain():
    loader = TextLoader("speech.txt")
    documents=loader.load()
    
    splitter = CharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    chunks=splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

    
    llm = OllamaLLM(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain

def main():
    qa_chain = build_qa_chain()
    
    print("Ask a question related to Dr. Ambedkar's speech (type 'exit' to quit):")
    
    while True:
        query =input("\n Your question:")
        if query.lower() in ["exit","quit"]:
            print("GoodBye!")
            break
        answer = qa_chain.invoke(query)
        print(f"\nAnswer: {answer}")
        
if __name__ == "__main__":
    main()
    