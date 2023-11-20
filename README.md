# Uncovering Insights in Audio: An Exploration

![RAG Over audio](/images/cover.png)


## Welcome!

Have you ever wondered what stories lie within the audio recordings around you? Perhaps you have an interview, a podcast, or a lecture that you wish you could dive into more deeply? This "Uncovering Insights in Audio" project is here to guide you on a journey of discovery, using a friendly and accessible approach to explore the richness of audio data.

## Why Audio Analysis?

Audio carries a wealth of information, but unlocking its secrets can be challenging. This project introduces you to a process that takes your audio content and helps you turn it into readable text. Imagine being able to read and understand the content of your recordings, making it easier to find specific moments or gather insights from spoken words.

## The Power of Retrieval Augmented Generation

At the heart of this exploration is a fascinating concept called "Retrieval Augmented Generation" (RAG). Think of it as a tool that not only transcribes your audio into text but also goes a step further. RAG enables you to ask questions about the transcribed content, as if you were interacting with a knowledgeable companion.

Instead of drowning in a sea of words, RAG allows you to retrieve specific information and generate new insights. It's like having a conversation with your audio data, turning it from a passive recording into an interactive resource.

## How Does It Work?

The process involves turning spoken words into written text (transcription) and then using a clever combination of technologies to make that text come alive. Through a series of steps, we encode the text with special markers, create a searchable database, and interact with it using a language model that can understand context and generate responses.

## What to Expect

In this project, you'll find a Jupyter notebook named `rag-over-whisper-audio.ipynb`. It's designed to be your friendly guide through the steps of loading your audio data, transforming it into text, and using RAG to pose questions and receive insightful answers.

No need to worry about complex technical jargon – this journey is crafted for those curious minds who want to explore the potential hidden within their audio recordings.

Ready to embark on this audio adventure? Let's start uncovering insights together!

The notebook primarily illustrates how to:
1. Load and examine audio-derived text data.
2. Use Ollama embeddings to encode the data.
3. Create a vector store with FAISS for efficient similarity search.
4. Prompt a large language model (LLM), such as Llama2, using context from the vector store.
5. Perform a question-answering task based on the text data and embedded context.

## Prerequisites
- Python 3
- Jupyter Notebook or JupyterLab
- Required Python libraries: `ollama`, `faiss`, `langchain`

## Installation
1. Ensure you have Python 3 installed.
2. Clone this repository or download the Jupyter notebook file.
3. Open the Jupyter notebook in VSCode (I use the Jupyter extension in VSCode), JupyterLab or Jupyter Notebook environment.
4. Install required Python libraries using `pip` or `conda`.

    ```bash
    pip install ollama faiss-cpu langchain
    ```

    or if you need to specify Python 3:

    ```bash
    python3 -m pip install ollama faiss-cpu langchain
    ```

    or

    ```bash
    conda install -c pytorch faiss-cpu
    pip install ollama langchain
    ```

## Usage
In the `rag-over-whisper-audio.ipynb` notebook:
- Run the cells in sequential order. *(Note: The way you run a cell is by pressing shift enter)*
- The notebook will guide you through loading the audio-derived text data, creating embeddings, and setting up FAISS to create a vector store.
- It will then walk you through the process of using a Large Language Model (LLM) with a chain designed for question-answering tasks.
- Example queries can be modified to retrieve relevant information from the encoded text data.
- The notebook demonstrates a vector similarity search based on a query and how to use the result in the context of generating a response from the LLM.

## Contributing
For any improvements or bug reports, please open an issue or make a pull request in this repository.

Note: This README is a high-level abstraction of the Jupyter notebook. For detailed explanation and execution, refer to the actual notebook provided in this repository.


## Examples

To give you a taste of what's possible, here an example usage of the notebook:

**Understand Key Ideas from a 1926 Trade Union Speech**: 

![A.J.Cook](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/AJ_Cook.webp/220px-AJ_Cook.webp.png)

This is [Mr. A.J. Cook](https://en.wikipedia.org/wiki/A._J._Cook_(trade_unionist)) - a prominent figure in the British Labour Party and a key figure in the General Strike of 1926. He gave a speech on the 1st of December 1926. We can use Retreival Augmented Generation - or RAG - to understand the key ideas from the speech. His speech can be found on [wikipedia](https://commons.wikimedia.org/wiki/File:A_J_Cook_Speech_from_Lansbury%27s_Labour_Weekly.ogg)

Let's start by defining a question we want to answer:
   
    
    query = "What is the idea of the republic?"
    

Next, we can do a semantic similarity search for documents with similar content to the query. Semantic similarity is a measure of the degree to which two pieces of text carry the same meaning. We can also print out these documents:
    
    
    docs = docsearch.similarity_search(query)
    print(docs)
    

Which reveals the following chunks of text that are similar to the query: 

    
    [Document(page_content='among men to secure these rights, and that governments derive their just powers from the consent of', metadata={'source': '5'}),
    Document(page_content='weight of their own armaments. A republic whose flag is loved by other flags are only tears. The', metadata={'source': '11'}),
    Document(page_content='propaming to the world the self-evident propositions that all men are created equal, that they are', metadata={'source': '3'}),
    Document(page_content='the coming of a universal brotherhood. A republic which shakes roads and dissolves their', metadata={'source': '14'})]
    

Then we take these text chunks, and the query together to generate a response. This is the RAG step - our query is semantically compared to our document chunks, and we *Retrive* the top several semantically similar chunks. These then *Augment* our query to enable us to *Generate* a response - there you have it: *RAG*!

     
    response = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
    print(response["output_text"])
    
Which gives us the following response:

    
> Based on the context provided, it seems that the idea of the republic is centered around the concept of democracy and the belief that governments derive their power from the consent of the governed. The republic is seen as a way to secure individual rights and promote equality among citizens, with the ultimate goal of creating a universal brotherhood. Additionally, the flag of the republic is seen as a symbol of hope and progress, representing the idea that all men are created equal and have the right to be heard.

Now we know more about Cook's speech!

**Thanks for staying with me until the end! We now we know more about the key ideas from the speech!**