# RAG related
This folder contains RAG-related scripts and tips.

## enterprise_json2md.py
This script aims at converting the Mitre ATT&CK Enterprise json file into Markdown for ease of use as RAG "Knowledge Base".
The md file can then be used as a knowledge base in Open WebUI for example to leverage RAG feature. The script doesn't create chunk/vector. This part is handled by Open WebUI at import. 

### Uploading the MITRE ATT&CK Markdown as a new Knowledge base in Open WebUI

![image](https://github.com/user-attachments/assets/e5db3c82-d056-408d-84d2-ff0aed3b05d3)

### Creating a custom model with RAG to the Mitre ATT&CK KB

![image](https://github.com/user-attachments/assets/d4ed2b67-ffff-4172-9afe-794430b9a324)

### Referencing the collection (KB) in your prompt with any model

![image](https://github.com/user-attachments/assets/9bfa0da9-d2d9-400b-871d-11cbe6d91b70)
