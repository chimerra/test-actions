# FastAPI Time Server

A simple FastAPI application that returns the current server time with automated Docker deployment via GitHub Actions.

## Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /time` - Returns current server time in multiple formats
- `GET /health` - Health check endpoint

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn main:app --reload
```

3. Access the API:
   - API will be available at `http://localhost:8000`
   - Interactive docs at `http://localhost:8000/docs`

## Docker Deployment

The GitHub Actions workflow automatically builds and pushes the Docker image to GitHub Container Registry when code is pushed to the `main` branch.

### Manual Docker Build

```bash
# Build the image
docker build -t fastapi-time-server .

# Run the container
docker run -p 8000:8000 fastapi-time-server
```

### Pull from GitHub Container Registry

```bash
# Pull the image (replace with your repository name)
docker pull ghcr.io/your-username/github_actions:latest

# Run the container
docker run -p 8000:8000 ghcr.io/your-username/github_actions:latest
```

## GitHub Actions Workflow

The workflow `.github/workflows/deploy.yml`:

- Triggers on push to `main` branch
- Builds Docker image using the provided Dockerfile
- Pushes the image to GitHub Container Registry (ghcr.io)
- Uses automatic tagging based on branch and commit SHA
- Includes build caching for faster builds

## API Response Examples

### GET /time
```json
{
  "current_time": "2026-03-23T20:52:00.123456",
  "timestamp": 1711224720.123456,
  "formatted": "2026-03-23 20:52:00"
}
```

### GET /health
```json
{
  "status": "healthy",
  "timestamp": "2026-03-23T20:52:00.123456"
}
```
