# 🚀 FormDyn API

A **FormDyn API** é uma aplicação backend construída com **FastAPI** para a **gestão de formulários dinâmicos**, permitindo a criação, versionamento e armazenamento de dados de forma **flexível, segura e escalável**.

---

## 📌 Visão Geral

- 🧩 **Projeto:** FormDyn API  
- 🏷️ **Versão:** 0.1.0  
- 📝 **Descrição:** Gestão de formulários dinâmicos para armazenamento de dados  
- 👤 **Autor:** Max Fernandes de Souza  
- ✉️ **E-mail:** xaamax@gmail.com  

---

## 🧱 Tecnologias Utilizadas

- 🐍 Python  
- ⚡ FastAPI  
- 🧪 Pytest  
- 📊 Coverage.py  
- 🧹 Ruff (lint + formatter)  
- 🛠️ Taskipy  
- 🌐 Uvicorn  

---

## 📂 Estrutura do Projeto

Estrutura atual do projeto conforme organização em camadas e domínios:

```text
app/
├── app.py                      # 🚪 Ponto de entrada da aplicação
├── core/                       # ⚙️ Núcleo da aplicação
│   ├── database.py             # 🗄️ Configuração de banco de dados
│   ├── exception_handlers.py   # 🚨 Handlers globais de exceções
│   ├── exceptions.py           # ❗ Exceções customizadas
│   └── models.py               # 📦 Modelos base / compartilhados
├── modules/                    # 🧠 Módulos de domínio
│   ├── answers/                # 📝 Respostas
│   ├── fields/                 # 🧩 Campos dinâmicos
│   ├── forms/                  # 📋 Formulários
│   ├── forms_answers/          # 🔗 Respostas por formulário
│   └── options_answers/        # ☑️ Opções de resposta
├── shared/                     # ♻️ Código compartilhado
│   ├── entity_base_model.py    # 🧱 Entidade base
│   ├── pagination.py           # 📄 Paginação
│   ├── repository_base.py      # 🗄️ Base de repositórios
│   └── schemas.py              # 📐 Schemas comuns
├── migrations/                 # 🧬 Migrações de banco de dados
├── docs/                       # 📘 Documentação (MkDocs)
└── tests/                      # 🧪 Testes automatizados
    ├── integration/            # 🔗 Testes de integração
    │   ├── answers/
    │   ├── fields/
    │   ├── forms/
    │   ├── forms_answers/
    │   └── options_answers/
    └── unit/                   # 🧩 Testes unitários
        ├── answers/
        ├── fields/
        ├── forms/
        ├── forms_answers/
        └── options_answers/
```

---

## ▶️ Executando a Aplicação

### 🧑‍💻 Ambiente de Desenvolvimento

```bash
task run
```

Ou:

```bash
fastapi dev app/app.py
```

### 🌍 Endpoints Padrão

- 🔗 **API:** http://localhost:8000  
- 📘 **Swagger:** http://localhost:8000/docs  
- 📕 **Redoc:** http://localhost:8000/redoc  

---

## 🧪 Testes Automatizados

### ▶️ Executar testes com cobertura

```bash
task tests
```

Ou:

```bash
pytest --cov=app --cov-report=term-missing
```

### ✅ Política de Qualidade

- 📈 Cobertura mínima exigida: **90%**
- ❌ A execução falha se a cobertura mínima não for atingida

---

## 🧹 Qualidade de Código

### 🔍 Verificar lint

```bash
task lint
```

### 🛠️ Corrigir lint e formatar

```bash
task lint_fix
```

### 🎨 Apenas formatar

```bash
task format
```

---

## ⚙️ Configuração do Ruff

- 📏 **Line length:** 79
- ✍️ **Aspas:** simples (`'`)
- 🚫 **Pastas ignoradas:** `migrations`
- ✅ **Regras ativas:** `I`, `F`, `E`, `W`, `PL`, `PT`
- 🧪 **Exceções:** `E501`, `PLR2004` (em testes)

---

## 📊 Cobertura de Código

### 🚫 Arquivos excluídos

```text
app/core/*
app/shared/repository_base.py
app/modules/*/repository.py
```

Arquivos de **infraestrutura** não entram no cálculo de cobertura.

---

## 🏗️ Padrões Arquiteturais

- 🧩 Separação por módulos de domínio
- 🧠 Serviços e regras de negócio desacoplados
- 🗄️ Repositórios para persistência
- 🔌 Infraestrutura isolada
- 🧪 Testes unitários e de integração bem definidos
- 📘 Documentação automática via OpenAPI

---

## ✨ Boas Práticas

- 🧾 Tipagem explícita
- 📐 Validação com Pydantic
- 🚨 Tratamento centralizado de exceções
- 🧹 Código padronizado via Ruff
- 🛡️ Qualidade garantida por testes

---

## 🚀 Próximos Passos

- 🔐 Autenticação (JWT / OAuth2)
- 🏷️ Versionamento de formulários
- 🕵️ Auditoria de alterações
- ⚡ Cache com Redis
- 🐳 Dockerização
- 🔄 CI/CD

---

## 📄 Licença

🔒 Projeto de uso privado.  
📬 Entre em contato com o autor para mais informações.
