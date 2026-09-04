import openwakeword
from openwakeword.model import Model

# Automatically fetch missing ONNX model weights on startup
openwakeword.utils.download_models()

print("Initializing openWakeWord...")
wakeword_model = Model(wakeword_models=["hey_jarvis"], inference_framework="onnx")