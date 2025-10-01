# FastAPI Vercel Application

A simple FastAPI application designed for deployment on Vercel, providing a REST API with health check functionality.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs with Python
- **Vercel Deployment**: Optimized for serverless deployment on Vercel
- **Health Check Endpoint**: Built-in health monitoring endpoint
- **Environment Configuration**: Configurable via environment variables
- **Auto-reload**: Development server with hot reload functionality

## 📁 Project Structure

```
fastapi-vercel/
├── app/
│   └── api.py          # Main FastAPI application
├── main.py             # Local development server
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel deployment configuration
└── README.md          # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-vercel
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file** (optional)
   ```bash
   # Create .env file in the root directory
   PORT=8000
   ```

## 🚀 Running the Application

### Local Development

Run the development server with auto-reload:

```bash
python main.py
```

The API will be available at:
- **Base URL**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

### Using Uvicorn Directly

Alternatively, you can run the application directly with uvicorn:

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

## 📡 API Endpoints

### `GET /`
Welcome endpoint that returns a greeting message.

**Response:**
```json
{
  "msgs": "Welcome to my api."
}
```

### `GET /api/health`
Health check endpoint for monitoring application status.

**Response:**
```json
{
  "status": "healthy"
}
```

## 🌐 Deployment on Vercel

This application is configured for easy deployment on Vercel.

### Deploy to Vercel

1. **Install Vercel CLI** (if not already installed)
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

### Deployment Configuration

The `vercel.json` file contains the deployment configuration:

- **Runtime**: `@vercel/python`
- **Entry Point**: `app/api.py`
- **Max Lambda Size**: 15MB
- **Routes**: All requests are routed to the FastAPI application

### Environment Variables

You can set environment variables in the Vercel dashboard:

- `PORT`: Server port (default: 8000)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port number | `8000` |

### Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **python-dotenv**: Environment variable management

## 🧪 Testing

You can test the API endpoints using curl or any HTTP client:

```bash
# Test welcome endpoint
curl http://localhost:8000/

# Test health check
curl http://localhost:8000/api/health
```

## 📝 Development

### Adding New Endpoints

Add new routes in `app/api.py`:

```python
@app.get("/api/new-endpoint")
def new_endpoint():
    return {"message": "New endpoint"}
```

### Adding Dependencies

1. Add the package to `requirements.txt`
2. Install locally: `pip install <package-name>`
3. Import and use in your application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vercel Documentation](https://vercel.com/docs)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Change the PORT environment variable or kill the process using the port
2. **Module not found**: Ensure all dependencies are installed (`pip install -r requirements.txt`)
3. **Vercel deployment fails**: Check that `vercel.json` configuration is correct and all files are committed

### Getting Help

If you encounter any issues, please:
1. Check the existing issues in the repository
2. Create a new issue with detailed information about the problem
3. Include error messages and steps to reproduce the issue