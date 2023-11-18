# Rag Over Whisper Audio Analysis

This repository contains a Jupyter notebook `rag-over-whisper-audio.ipynb` which demonstrates an analysis of audio data, leveraging the capabilities of Ollama embeddings, FAISS similarity search, and Language Model (LLM) chains for natural language processing tasks.

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
3. Open the Jupyter notebook in JupyterLab or Jupyter Notebook environment.
4. Install required Python libraries using `pip` or `conda`.

    ```bash
    pip install ollama faiss-cpu langchain
    ```

    or

    ```bash
    conda install -c pytorch faiss-cpu
    pip install ollama langchain
    ```

## Usage
In the `rag-over-whisper-audio.ipynb` notebook:
- Run the cells in sequential order.
- The notebook will guide you through loading the audio-derived text data, creating embeddings, and setting up FAISS to create a vector store.
- It will then walk you through the process of using a Large Language Model (LLM) with a chain designed for question-answering tasks.
- Example queries can be modified to retrieve relevant information from the encoded text data.
- The notebook demonstrates a vector similarity search based on a query and how to use the result in the context of generating a response from the LLM.

## Contributing
For any improvements or bug reports, please open an issue or make a pull request in this repository.

## License
Please refer to the licensing information of the used libraries and frameworks. The project itself does not mention a specific license, so it is advisable to assume a default copyright based on your local laws until clarified with the repository owner.

## Authors
- The notebook does not reveal the author's name but it likely involves contributions from experts in the fields of NLP, machine learning, and audio analysis.

Note: This README is a high-level abstraction of the Jupyter notebook. For detailed explanation and execution, refer to the actual notebook provided in this repository.