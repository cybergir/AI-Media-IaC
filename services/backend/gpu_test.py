import torch

print("===== System Information =====")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
print(f"cuDNN version: {torch.backends.cudnn.version()}")

print("\n===== GPU Availability =====")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Device count: {torch.cuda.device_count()}")

if torch.cuda.is_available():
    current_device = torch.cuda.current_device()
    print(f"\n===== GPU Details =====")
    print(f"Current device: {current_device}")
    print(f"Device name: {torch.cuda.get_device_name(current_device)}")
    print(f"Device capability: {torch.cuda.get_device_capability(current_device)}")
    print(f"Device memory: {torch.cuda.get_device_properties(current_device).total_memory/1024**3:.2f} GB")
else:
    print("\nCUDA not available. Potential issues:")
    print("1. NVIDIA drivers not installed")
    print("2. CUDA toolkit not installed")
    print("3. PyTorch not built with CUDA support")
    print("4. GPU not detected by system")