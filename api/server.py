import uvicorn
from main import app
from auth.routes import AuthRoutes

app.include_router(AuthRoutes)


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port = 8000, reload=True)