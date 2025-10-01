# FastAPI Vercel Application

A simple FastAPI application designed for deployment on Vercel, providing a REST API with health check functionality.

## 🚀 Features

- **FastAP## 🔧 ConfigurationModern, fast web framework for building APIs with Python
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

This application is optimized for deployment on Vercel with automatic Git integration.

### Vercel Project Configuration

#### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Go to [vercel.com](https://vercel.com) and sign up/login**

2. **Import your project:**
   - Click "New Project"
   - Import from your GitHub repository
   - Select `masudpervez27/fastapi-vercel`

3. **Configure project settings:**
   - **Framework Preset**: `Other`
   - **Root Directory**: Leave empty (project is at repository root)
   - **Build Command**: Leave empty (Vercel auto-detects from `vercel.json`)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Deploy**: Click "Deploy" and your app will be live in minutes!

#### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

### Automatic Git Integration

Once your project is connected to Vercel:

- **Automatic Deployments**: Every push to your main/master branch triggers a new deployment
- **Preview Deployments**: Pull requests get their own preview URLs
- **Zero Configuration**: No additional setup needed after initial connection
- **Instant Rollbacks**: Easy to revert to previous deployments from Vercel dashboard
- **Build Logs**: Detailed logs for troubleshooting deployment issues

### Vercel Project Settings

**Important Configuration Notes:**

- **Root Directory**: Must be left empty since your project files are at the repository root
- **Environment Variables**: Set these in Vercel dashboard under Settings → Environment Variables
- **Custom Domains**: Configure under Settings → Domains
- **Build & Output Settings**: Handled automatically by `vercel.json`

### Deployment Configuration

The `vercel.json` file contains the deployment configuration:

- **Runtime**: `@vercel/python`
- **Entry Point**: `app/api.py`
- **Max Lambda Size**: 15MB
- **Routes**: All requests are routed to the FastAPI application

### Environment Variables

You can set environment variables in the Vercel dashboard:

- `PORT`: Server port (default: 8000)

## � CI/CD Pipeline

This project includes automated deployment using GitHub Actions. Every push to the main branch triggers:

1. **Code Checkout**: Retrieves the latest code from the repository
2. **Vercel Deployment**: Automatically deploys to Vercel using the official Vercel Action
3. **Live URL**: Provides a live URL for the deployed application

### Workflow Features
- **Automatic deployment** on push to main branch
- **Zero-configuration** deployment process
- **Secure secrets management** through GitHub repository secrets
- **Build status visibility** through GitHub Actions interface

## �🔧 Configuration

### Environment Variables

| Variable | Description | Default | Where to Set |
|----------|-------------|---------|--------------|
| `PORT` | Server port number | `8000` | Local: `.env` file, Vercel: Dashboard Settings |

### Vercel Environment Variables

Set environment variables in your Vercel project dashboard:
1. Go to your project dashboard on Vercel
2. Navigate to **Settings → Environment Variables**
3. Add your variables for different environments (Production, Preview, Development)

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