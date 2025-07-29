# Use official Triton image
FROM nvcr.io/nvidia/tritonserver:22.04-py3

USER root
RUN echo "root:foooooooo" | chpasswd

# Create model repository and directory structure
RUN mkdir -p /models/model_onnx/1
RUN mkdir -p /models/malicious_onnx/1

# Copy model files into the container
COPY ./model_onnx/model.onnx /models/model_onnx/1/model.onnx
COPY ./model_onnx/config.pbtxt /models/model_onnx/config.pbtxt

# Cop another
COPY ./malicious_onnx/malicious.onnx /models/malicious_onnx/1/model.onnx
COPY ./malicious_onnx/config.pbtxt /models/malicious_onnx/config.pbtxt

# Expose default Triton ports
EXPOSE 8000

# Start Triton server with the model repo
CMD ["tritonserver", "--model-repository=/models", "--model-control-mode=explicit"]
