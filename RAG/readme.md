# RAG related
This folder contains RAG-related scripts and tips.

## enterprise_json2md.py
This script aims at converting the Mitre ATT&CK Enterprise json file into Markdown for ease of use as RAG "Knowledge Base".
The md file can then be used as a knowledge base in Open WebUI for example to leverage RAG feature. The script doesn't create chunk/vector. This part is handled by Open WebUI at import. 
