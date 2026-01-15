from fastapi import FastAPI

def app_fabric():
    app = FastAPI(
        debug=True,
        title="Vofga Auto Prom Orders",
        summary="Сервис для приема заказов на автомобильный запчасти ВолгаАвтоПром",
        openapi_url="/api/docs")
    return app