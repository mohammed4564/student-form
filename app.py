from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.student_routes import router as student_router

app = FastAPI(
    title="Student Management API",
    description="Simple Student CRUD API",
    version="1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(student_router)


@app.get("/")
def home():

    return {"message": "Student API is running"}