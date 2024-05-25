from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Olá Mundo"}

@router.get("/api/itens")
def read_itens():
    return [{"item": "Item 1"}, {"item": "Item 2"}]
