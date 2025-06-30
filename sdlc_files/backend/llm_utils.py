from llama_cpp import Llama
from typing import Optional
MODEL_PATH = "C:/Users/Tarun/oose/granite/granite-3.3-2b-instruct-Q4_K_M (1).gguf"

# Initialize model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,      # Context window size
    n_threads=8,     # CPU threads (adjust to your core count)
    n_gpu_layers=0  # GPU offload layers (set to 0 for CPU-only)
)

def query_llm(
    prompt: str,
    max_tokens: int = 512,
    temperature: float = 0.7,
    stop: Optional[list] = None
) -> str:
    """
    Get a response from the LLM.
    
    Args:
        prompt: Your input text
        max_tokens: Response length limit
        temperature: 0.0-1.0 (lower = more deterministic)
        stop: List of strings to stop generation at
    
    Returns:
        Generated text (strip() removes leading/trailing whitespace)
    """
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    output = llm(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop or ["</s>", "User:", "AI:"]
    )
    return output["choices"][0]["text"].strip()

# Example usage
if __name__ == "__main__":
    response = query_llm("Explain quantum computing like I'm five")
    print(response)