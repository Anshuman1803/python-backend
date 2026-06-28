from fastapi import APIRouter;
router = APIRouter(
    tags= ["Home"]
)
@router.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}