# Rag Over Whisper Audio Analysis

![RAG Over audio](/images/cover.png)


## Welcome!

Have you ever wondered what stories lie within the audio recordings around you? Perhaps you have an interview, a podcast, or a lecture that you wish you could dive into more deeply? The "Uncovering Insights in Audio" project is here to guide you on a journey of discovery, using a friendly and accessible approach to explore the richness of audio data.

## Why Audio Analysis?

Audio carries a wealth of information, but unlocking its secrets can be challenging. This project introduces you to a process that takes your audio content and helps you turn it into readable text. Imagine being able to read and understand the content of your recordings, making it easier to find specific moments or gather insights from spoken words.

## The Power of Retrieval Augmented Generation

At the heart of this exploration is a fascinating concept called "Retrieval Augmented Generation" (RAG). Think of it as a tool that not only transcribes your audio into text but also goes a step further. RAG enables you to ask questions about the transcribed content, as if you were interacting with a knowledgeable companion.

Instead of drowning in a sea of words, RAG allows you to retrieve specific information and generate new insights. It's like having a conversation with your audio data, turning it from a passive recording into an interactive resource.

## How Does It Work?

The process involves turning spoken words into written text (transcription) and then using a clever combination of technologies to make that text come alive. Through a series of steps, we encode the text with special markers, create a searchable database, and interact with it using a language model that can understand context and generate responses.

## What to Expect

In this project, you'll find a Jupyter notebook named `uncover-audio-insights.ipynb`. It's designed to be your friendly guide through the steps of loading your audio data, transforming it into text, and using RAG to pose questions and receive insightful answers.

No need to worry about complex technical jargon – this journey is crafted for those curious minds who want to explore the potential hidden within their audio recordings.

Ready to embark on this audio adventure? Let's start uncovering insights together!

----

If you've wanted to play around with audio, RAG, and locally-run LLMs - this is a perfect starting point! 

This repository contains a Jupyter notebook `rag-over-whisper-audio.ipynb` which demonstrates an analysis of audio data, leveraging the capabilities of Ollama embeddings, FAISS similarity search, and open-source Large Language Model (LLM) chains. Loading in your own audio to this notebook enables you to ask questions about the information contained in your audio file completely locally.

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