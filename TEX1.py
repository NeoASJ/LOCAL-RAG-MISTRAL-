# from pdfminer.high_level import extract_text

# text = extract_text(r"C:\Users\HP\Downloads\resume (7).pdf")
# print(text)
# import fitz  # PyMuPDF

# def extract_text_pymupdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     full_text = ""
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         text = page.get_text()
#         full_text += text + "\n"
#     return full_text

# # Usage
# pdf_file = r"C:\Users\HP\Downloads\resume (7).pdf"
# text = extract_text_pymupdf(pdf_file)
# print(text)

# import re
# from nltk.tokenize import sent_tokenize

# def clean_text(text):
#     # Remove extra whitespace and newlines
#     text = re.sub(r'\s+', ' ', text)
#     # Remove non-printable characters (optional)
#     text = ''.join(c for c in text if c.isprintable())
#     # Remove unwanted characters like page numbers or headers (example pattern)
#     text = re.sub(r'Page \d+ of \d+', '', text, flags=re.IGNORECASE)
#     # Strip leading/trailing whitespace
#     text = text.strip()
#     return text

# def segment_text(text, chunk_size=300):
#     # Split into sentences
#     sentences = sent_tokenize(text)
    
#     # Combine sentences into chunks of approximately chunk_size words
#     chunks = []
#     current_chunk = []
#     current_length = 0
    
#     for sent in sentences:
#         words = sent.split()
#         if current_length + len(words) > chunk_size:
#             chunks.append(' '.join(current_chunk))
#             current_chunk = words
#             current_length = len(words)
#         else:
#             current_chunk.extend(words)
#             current_length += len(words)
#     # Add last chunk
#     if current_chunk:
#         chunks.append(' '.join(current_chunk))
    
#     return chunks

# # Usage example
# raw_text = text
# cleaned_text = clean_text(raw_text)
# text_chunks = segment_text(cleaned_text)

# for i, chunk in enumerate(text_chunks):
#     print(f"Chunk {i+1}: {chunk[:10]}...")  # Print first 100 chars of each chunk
# print('-----------------------------------------------------------------------')
# print('len of og',len(text))
# print('len of rewrkg',len(cleaned_text))
# from sentence_transformers import SentenceTransformer

# # Load pre-trained SBERT model
# model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast, and accurate

# # Sample text chunks (from your earlier preprocessing)
# text_chunks = [
#     "This is the first chunk of text extracted from a PDF document.",
#     "Here is the second chunk containing different information.",
# ]

# # Convert text chunks to embeddings (vectors)
# embeddings = model.encode(text_chunks)

# # embeddings is a list of vectors, one for each chunk
# print(f"Embedding for first chunk (vector length: {len(embeddings[0])}):")
# print(embeddings)
# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Sample text chunks (e.g., from your PDF)
# text_chunks = [
#     "Artificial intelligence is the simulation of human intelligence by machines.",
#     "Machine learning is a subset of AI focused on training models with data.",
#     "Deep learning uses neural networks to solve complex tasks.",
#     "AI has many applications including natural language processing and computer vision."
# ]

# # Load pre-trained Sentence-BERT model for embeddings
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Generate embeddings for text chunks
# embeddings = model.encode(text_chunks)
# embedding_dim = embeddings.shape[1]

# # Convert embeddings to float32 numpy array
# embedding_matrix = np.array(embeddings).astype('float32')

# # Create FAISS index for L2 similarity search
# index = faiss.IndexFlatL2(embedding_dim)
# index.add(embedding_matrix)  # Add embeddings to the index

# # Query text
# query = "What is artificial intelligence?"
# query_embedding = model.encode([query])[0].reshape(1, -1).astype('float32')

# # Search for top 2 most similar chunks
# k = 2
# distances, indices = index.search(query_embedding, k)

# print(f"Top {k} relevant text chunks for query: '{query}'\n")
# for rank, idx in enumerate(indices[0]):
#     print(f"Rank {rank+1}:")
#     print(f"Text: {text_chunks[idx]}")
#     print(f"Distance: {distances[0, rank]:.4f}\n")


from transformers import pipeline

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering")

# Sample context (this would be the retrieved text chunks combined)
context = """
Artificial intelligence is the simulation of human intelligence by machines. 
It has many applications including natural language processing and computer vision.
"""

# The question you want answered based on the context
question = "What is artificial intelligence?"

# Get answer from the pipeline
result = qa_pipeline(question=question, context=context)

# Print the answer
print(f"Answer: {result['answer']}")

