from peft import get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch


model_name = "mistralai/Mistral-7B-Instruct-v0.3"
quantization_config  = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_enable_fp32_cpu_offload=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config ,
    device_map="auto",
    trust_remote_code=True
)