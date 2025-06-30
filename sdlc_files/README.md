# SmartSDLC: AI-Powered SDLC Automation Platform

SmartSDLC is an AI-powered Software Development Lifecycle Automation Platform that helps with requirement analysis, design generation, code generation and explanation, testing, and provides a chatbot assistant for SDLC-related queries.

## Features

- 📝 **Requirement Analysis**: Extract requirements from PDFs and custom prompts
- 📐 **Design**: Generate design docs, UML diagrams, or summaries
- 💻 **Coding**: Generate code, explain code in multiple languages
- 🧪 **Testing**: Generate test cases, detect and fix bugs
- 💬 **Chatbot Assistant**: Ask anything about SDLC, coding, and more

## Technology Stack

- **Backend**: FastAPI, Python
- **Frontend**: Streamlit
- **AI Model**: IBM Granite 3.3_2b Instruct (via llama-cpp-python)
- **PDF Processing**: PyPDF2

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. IBM Granite 3.3_2b Instruct model file (`granite-3.3-2b-instruct-Q4_K_M.gguf`)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Update the model path in `llm_utils.py` if necessary:
   ```python
   MODEL_PATH = "C:/Users/Tarun/oose/sdlc_r1_model/granite-3.3-2b-instruct-Q4_K_M.gguf"
   ```

6. Run the backend server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Usage

1. Start the backend server (FastAPI will run on `http://localhost:8000`)
2. Start the frontend (Streamlit will run on `http://localhost:8501`)
3. Access the application through your web browser
4. Use the sidebar navigation to access different features

## API Endpoints

- `POST /analyze-requirements/`: Analyze requirements from PDF
- `POST /generate-design/`: Generate design documents
- `POST /generate-code/`: Generate code from requirements
- `POST /explain-code/`: Explain existing code
- `POST /generate-tests/`: Generate test cases
- `POST /fix-bug/`: Detect and fix bugs
- `POST /chat/`: Chat with AI assistant

## File Structure

```
sdlc_PTO/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── schemas.py        # Pydantic models
│   ├── pdf_utils.py      # PDF processing utilities
│   ├── llm_utils.py      # LLM interaction utilities
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── app.py           # Streamlit application
│   ├── ui_utils.py      # UI styling utilities
│   └── requirements.txt # Python dependencies
└── README.md           # This file
```

## Configuration

- Update `BACKEND_URL` in `frontend/app.py` if running on different host/port
- Adjust model parameters in `backend/llm_utils.py` based on your hardware
- Modify CORS settings in `backend/main.py` for production deployment

## Troubleshooting

1. **Model loading issues**: Ensure the model path is correct and the model file exists
2. **Connection errors**: Check that the backend is running and the URL is correct
3. **Memory issues**: Reduce `n_ctx` or `n_gpu_layers` in `llm_utils.py`

## License

This project is for educational purposes.
