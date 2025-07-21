# Build your Triton container
docker build -t my-triton .

# Run it with ports exposed
docker run --rm -p8000:8000 -p8001:8001 -p8002:8002 my-triton

# Use cmd below
curl -X POST localhost:8000/v2/models/model_onnx/infer \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": [
      {
        "name": "X",
        "shape": [2, 2],
        "datatype": "FP32",
        "data": [0.0, 0.0]
      }
    ],
    "outputs": [
      { "name": "Y" }
    ]
  }' | jq .

