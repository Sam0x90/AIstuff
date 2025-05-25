# AIstuff
All my AI-related stuff.
This repo collects tools, prompts, and experiments around LLMs, agents, RAG, CAG, MCP, and whatever acronym is trending this week. 
Hopefully something could be useful for the community and peers.
My focus is mainly cyber-related and I am focusing on running everything locally to avoid cloud/SaaS dependencies. 

## RAG
Experiments and utilities related to RAG setups.

Currently includes:
- A docling-style script that converts the [MITRE ATT&CK STIX repository](https://github.com/mitre-attack/attack-stix-data/) into Markdown files. Perfect (not really :D) for use with Open WebUI, just drag and drop as a new knowledge base and enable RAG-powered MITRE lookups for your local LLMs.

## Prompts
Collection of prompts for various purpose.

Currently includes:
- Prompt test cases to evaluate MITRE ATT&CK technique extraction accuracy via RAG-enabled LLMs. It comes with example inputs and expected outputs to benchmark different models or setups
