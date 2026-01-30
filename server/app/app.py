from fastapi import FastAPI

from .modules.fields.routers import router as field_routers
from .modules.forms.routers import router as form_routers

app = FastAPI(
    title='FormDyn API',
    description='API de Gestão de formulários dinâmicos',
    version='0.1.0',
)

app.include_router(form_routers)
app.include_router(field_routers)
