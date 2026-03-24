from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI(title="Time API", description="Simple API that returns current server time")

@app.get("/")
async def root():
    return {"message": "Time API is running"}

@app.get("/time")
async def get_server_time():
    """Returns the current server time"""
    current_time = datetime.now()
    return {
        "current_time": current_time.isoformat(),
        "timestamp": current_time.timestamp(),
        "formatted": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
