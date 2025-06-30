import os

MODEL_PATH = "C:/Users/Tarun/oose/sdlc_r1_model/granite-3.3-2b-instruct-Q4_K_M.gguf"

print(f"Checking model path: {MODEL_PATH}")
print(f"File exists: {os.path.exists(MODEL_PATH)}")

if os.path.exists(MODEL_PATH):
    print(f"File size: {os.path.getsize(MODEL_PATH) / (1024*1024*1024):.2f} GB")
else:
    print("Model file not found!")
    # List files in the directory
    directory = os.path.dirname(MODEL_PATH)
    if os.path.exists(directory):
        print(f"Files in {directory}:")
        for file in os.listdir(directory):
            print(f"  - {file}")