from huggingface_hub import snapshot_download
model_id="openai/gpt-oss-20b"
snapshot_download(repo_id=model_id, local_dir="./models/gpt-oss-20b",
                  local_dir_use_symlinks=False, revision="main")