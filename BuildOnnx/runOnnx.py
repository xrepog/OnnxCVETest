import onnxruntime as ort
import numpy as np

# Create an inference session
session = ort.InferenceSession("model.onnx")

# Prepare sample input
input_data = {
    "X": np.array([[10.0, 20.0], [30.0, 40.0]], dtype=np.float32)
}

# Run inference
outputs = session.run(None, input_data)
print(bytes(outputs[0]))

# Display the result
print("Output:")
print(outputs[0])
