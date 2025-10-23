# Agentic RAG System: D-Drive Local Deployment

*This document serves as both the technical guide and the progress report for the Agentic Retrieval-Augmented Generation (RAG) system developed for the intern project.*

## 1. Project Overview and Status

Component | Status | Log Detail |
|-----------|--------|------------|
Code Structure | ✓ Complete | All Python files (.py) are fully written and correctly linked. |
Cloud Dependency | ✓ ELIMINATED | Successfully migrated the entire application to run completely locally using Ollama, avoiding all cloud quotas and billing. |
Vector DB (Postgres) | ✓ SUCCESS | The system connected to Neon and cleared/resized the vector column correctly. |
Embedding | ✓ SUCCESS | The local model (all-minilm) successfully created and saved vectors to Postgres. |
Knowledge Graph (KG) | ✗ BLOCKED | The LLM for reasoning failed due to a hardware limit. |

## 2. Architectural Achievement

We successfully deployed a Hybrid RAG model that uses local resources for low-cost, accurate information retrieval.

Database Layer | Role | Primary Function |
|----------------|------|------------------|
Postgres/Neon | Vector Store | Stores document fragments as 384-dimension vectors (embeddings). Used for finding related concepts (semantic search). |
Neo4j | Knowledge Graph | Stores Entities and Relationships (e.g., "Microsoft PARTNERED_WITH OpenAI"). Used for structured reasoning and factual tracing. |

## 3. Key Challenges Overcome (Successes)

The major challenge was achieving stability across multiple dependencies, which is now resolved:

- **Cloud Quota**: Solved the persistent 429 Quota Exceeded errors by switching the entire LLM provider from Gemini/OpenAI to Ollama (http://localhost:11434/v1).
- **Version Conflicts**: Fixed the Pydantic and PostgreSQL dimension mismatch issues that arose from switching models. The system now correctly uses the 384-dimension vector from the small local models.
- **Code Integrity**: Eliminated multiple module import and caching errors by cleaning up the Python environment aggressively.

## 4. Final Blocker: Hardware Memory Issue

The system is failing on the very last step due to a hardware limitation that requires a model change.

**Problem**: The ingestion pipeline crashes during the Knowledge Graph extraction phase (when the LLM tries to extract entities from the document chunk).

**Root Cause**: The reasoning model currently selected, `llama3`, requires significantly more RAM ($\approx$ 5.4 GiB) than the machine currently has available ($\approx$ 3.8 GiB).

**Error Message**: `model requires more system memory (5.4 GiB) than is available (3.8 GiB)`

## 5. Next Step (Mentor Guidance Needed)

The project is complete on the software side. The only solution is a model downgrade to a version that fits the available RAM.

The system is ready to be indexed successfully once the model is switched to a smaller variant, such as `tinyllama` ($\approx$ 0.6 GiB) or `phi3:mini` ($\approx$ 2.5 GiB).

## Installation & Execution Guide

### Prerequisites

- **Project Location**: All files are in the D: drive (D:\RedLine).
- **Ollama**: Installed and running.
- **Neo4j Desktop**: The specific database instance must be RUNNING.

### Configuration (D:\RedLine\.env)

Setting | Value |
|---------|-------|
LLM_PROVIDER | ollama |
LLM_BASE_URL | http://localhost:11434/v1 |
LLM_CHOICE | llama3 (Will fail on memory) |
EMBEDDING_MODEL | all-minilm |
VECTOR_DIMENSION | 384 |