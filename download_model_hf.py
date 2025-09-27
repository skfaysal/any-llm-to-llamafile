import os
from dotenv import load_dotenv
from huggingface_hub import snapshot_download

# Load environment variables from .env file
load_dotenv()

model_id = "google/gemma-3-4b-it"
snapshot_download(
    repo_id=model_id, 
    local_dir="./models/gemma-3-4b-it",
    local_dir_use_symlinks=False, 
    revision="main",
    token=os.getenv("HUGGINGFACE_HUB_TOKEN")  # Read token from .env
)