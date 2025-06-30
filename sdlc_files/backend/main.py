from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from schemas import *
import pdf_utils
import llm_utils

app = FastAPI(
    title="SmartSDLC Backend",
    description="AI-powered SDLC Automation Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-requirements/", response_model=RequirementAnalysisResponse)
async def analyze_requirements(
    file: UploadFile = File(...),
    prompt: str = Form("")
):
    pdf_bytes = await file.read()
    text = pdf_utils.extract_text_from_pdf(pdf_bytes)
    combined_prompt = (
        "You are an expert business analyst. Carefully read the following "
        "software requirements document. "
        "Extract all functional and non-functional requirements, and classify "
        "them clearly. "
        "If the user provides additional instructions, follow them. "
        f"\n\nDocument Content:\n{text}\n"
    )
    if prompt.strip():
        combined_prompt += f"\nAdditional user instructions: {prompt}\n"
    combined_prompt += (
        "\n\nReturn the requirements as a markdown bullet list, grouped by "
        "'Functional Requirements' and 'Non-Functional Requirements' if possible."
    )
    # Higher tokens for comprehensive requirement analysis
    response = llm_utils.query_llm(combined_prompt, max_tokens=800, temperature=0.3)
    requirements = [line.strip("-• ") for line in response.splitlines() if line.strip()]
    return RequirementAnalysisResponse(requirements=requirements)

@app.post("/generate-design/", response_model=DesignResponse)
async def generate_design(request: DesignRequest):
    prompt = (
        f"You are a senior software architect. Based on the following project "
        f"description, generate a concise and clear {request.design_type.lower()}. "
        "Use best practices for modern software design. "
        "If the user requests a UML diagram, provide it in PlantUML text "
        "format. "
        "If a summary is requested, focus on key components and interactions."
        f"\n\nProject Description:\n{request.prompt.strip()}\n"
    )
    # Very high tokens for detailed design documents
    design = llm_utils.query_llm(prompt, max_tokens=1200, temperature=0.4)
    return DesignResponse(design=design.strip())

@app.post("/generate-code/", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    prompt = (
        f"You are an experienced software engineer. Write clean, well-"
        f"structured {request.language} code to implement the following requirement. "
        "Include comments and follow best practices. Only output the code, no "
        "explanations."
        f"\n\nRequirement:\n{request.prompt.strip()}\n"
    )
    # High tokens for code generation
    code = llm_utils.query_llm(prompt, max_tokens=1000, temperature=0.2)
    return CodeGenerationResponse(code=code.strip())

@app.post("/explain-code/", response_model=CodeExplanationResponse)
async def explain_code(request: CodeExplanationRequest):
    prompt = (
        f"You are a senior developer. Explain in detail what the following "
        f"{request.language} code does, including its purpose, logic, and any important "
        "functions or classes. "
        "Structure your explanation for someone with intermediate programming "
        "knowledge."
        f"\n\nCode:\n{request.code.strip()}\n"
    )
    # Medium-high tokens for detailed explanations
    explanation = llm_utils.query_llm(prompt, max_tokens=800, temperature=0.3)
    return CodeExplanationResponse(explanation=explanation.strip())

@app.post("/generate-tests/", response_model=TestCaseGenerationResponse)
async def generate_tests(request: TestCaseGenerationRequest):
    prompt = (
        f"You are a software test engineer. Generate comprehensive unit test "
        f"cases in {request.language} for the following code. "
        "Use best practices for test structure and naming. Only output the "
        "test code."
        f"\n\nCode to test:\n{request.code.strip()}\n"
    )
    # High tokens for comprehensive test suites
    test_cases = llm_utils.query_llm(prompt, max_tokens=1000, temperature=0.2)
    return TestCaseGenerationResponse(test_cases=test_cases.strip())

@app.post("/fix-bug/", response_model=BugFixResponse)
async def fix_bug(request: BugFixRequest):
    prompt = (
        f"You are a code reviewer. The following {request.language} code "
        "contains one or more bugs. "
        "Identify and fix all issues. Output the corrected code first, then "
        "provide a brief explanation of the changes."
        f"\n\nBuggy code:\n{request.code.strip()}\n"
        "\n\nFormat your response as:\n[Corrected Code]\nExplanation: [Your "
        "explanation here]"
    )
    # Medium tokens for bug fixes with explanations
    response = llm_utils.query_llm(prompt, max_tokens=700, temperature=0.2)
    if "Explanation:" in response:
        code, explanation = response.split("Explanation:", 1)
    else:
        code, explanation = response, ""
    return BugFixResponse(fixed_code=code.strip(), explanation=explanation.strip())

@app.post("/chat/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    history = "\n".join(request.history) if request.history else ""
    prompt = (
        "You are a helpful and knowledgeable AI assistant for software "
        "development projects. "
        "Answer the user's question clearly and concisely. If the question is "
        "about SDLC, programming, design, testing, or best practices, provide practical "
        "advice and examples when possible."
        f"\n\nConversation history:\n{history}\nUser: {request.message}\nAI:"
    )
    # Lower tokens for conversational responses
    response = llm_utils.query_llm(prompt, max_tokens=400, temperature=0.6)
    return ChatResponse(response=response.strip())