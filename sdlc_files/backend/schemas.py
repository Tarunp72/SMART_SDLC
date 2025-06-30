from pydantic import BaseModel
from typing import List, Optional

class RequirementAnalysisResponse(BaseModel):
    requirements: List[str]

class DesignRequest(BaseModel):
    prompt: str
    design_type: str

class DesignResponse(BaseModel):
    design: str

class CodeGenerationRequest(BaseModel):
    prompt: str
    language: str

class CodeGenerationResponse(BaseModel):
    code: str

class CodeExplanationRequest(BaseModel):
    code: str
    language: str

class CodeExplanationResponse(BaseModel):
    explanation: str

class TestCaseGenerationRequest(BaseModel):
    code: str
    language: str

class TestCaseGenerationResponse(BaseModel):
    test_cases: str

class BugFixRequest(BaseModel):
    code: str
    language: str

class BugFixResponse(BaseModel):
    fixed_code: str
    explanation: Optional[str]

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[str]] = []

class ChatResponse(BaseModel):
    response: str
