# Reranker Service (BAAI / FastAPI)

A **production-style reranker service** built with **FastAPI** and **BAAI cross-encoder rerank model**, designed for **RAG pipelines**.

This service loads the rerank model **once at startup** (GPU or CPU), runs **fully offline**, and exposes a simple HTTP API to rerank documents based on a query.

---

## 🚀 Features

- ✅ Cross-encoder reranking (BAAI `bge-reranker-base`)
- ✅ FastAPI-based HTTP service
- ✅ GPU acceleration (CUDA) with CPU fallback
- ✅ Fully offline after initial model download
- ✅ Clean Architecture separation
- ✅ Environment-based configuration
- ✅ Production-ready model lifecycle (load once, reuse)

---

## 📁 Project Structure
```
reranker/
├── app/
│ └── main.py # FastAPI entrypoint
│
├── internal/
│ ├── config/ # Configuration & model initialization
│ ├── domain/ # Core domain entities (e.g. Document)
│ ├── infra/ # External integrations (ML models, clients)
│ ├── repository/ # Data access abstractions (optional)
│ ├── response/ # API response DTOs (Pydantic models)
│ ├── transport/ # HTTP / controller layer
│ └── usecase/ # Business logic (rerank usecase)
│
└── README.md
```

### Layer Responsibilities
```
|           Layer         |             Responsibility             |
|------------------------------------------------------------------|
| `domain`                | Pure business entities (no FastAPI / no Pydantic)
| `usecase`               | Core rerank logic
| `infra`                 | ML model, external services
| `transport`             | FastAPI routes & controllers
| `response`              | Pydantic response schemas
| `config`                | Environment variables & model bootstrapping
```