from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="Student Management API",
    description="Simple Student CRUD API",
    version="1.0"
)

# Register routes
app.include_router(student_router)


@app.get("/")
def home():

    return {"message": "Student API is running"}