from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Product Finder API is running!"}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    # Simulate search and return fake link
    filename = file.filename
    return {
        "filename": filename,
        "status": "success",
        "link": "https://www.amazon.in/example-product"
    }
