from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.exception_handlers import generic_exception_handler

from .modules.answers.routers import router as answer_routers
from .modules.fields.routers import router as field_routers
from .modules.forms.routers import router as form_routers
from .modules.forms_answers.routers import router as form_answer_routers
from .modules.options_answers.routers import router as option_answer_routers

app = FastAPI(
    title='FormDyn API',
    description='API de Gestão de formulários dinâmicos',
    version='0.1.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(form_routers)
app.include_router(field_routers)
app.include_router(answer_routers)
app.include_router(option_answer_routers)
app.include_router(form_answer_routers)
