# any-llm-to-llamafile
Toolkit to convert any opensource llm to executable server


## Convert HF models to `.gguf`
Models can be downloaded manually or using
`download_model_hf.py`

```bash
## Clone llama.cpp
git@github.com:ggml-org/llama.cpp.git

## Install dependencies
cd llama.cpp
pip install -r requirements.txt
cd ..

# Convert hf .safetensors model to .gguf
python3 llama.cpp/convert_hf_to_gguf.py models/llama-3.2-3b-instruct \
  --outfile checkpoints/llama-3.2-3b-instruct.gguf \
  --outtype f16

```

## Expose  GGUF as localhost using `llama-serve`

### Install [llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md) 

```bash
brew install llama.cpp
```

```bash
```bash
llama-serve \
  --model ./checkpoints/llama-3.2-3b-instruct.gguf \
  --ctx_size 128000 \
  --port 8000 \
  --threads 8
  
## Server
#It will open a chat ui in `http://127.0.0.1:8000/`
```

### Python usage
```bash
python3 test_python_api.py
```