curl -X POST localhost:8000/v2/models/model_onnx/infer   -H "Content-Type: application/json"   -d '{
    "inputs": [
      {
        "name": "X",
        "shape": [4, 10],
        "datatype": "FP32",
        "data": [[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                 [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
      }
    ],
    "outputs": [
      { "name": "Y" }
    ]
  }' | jq .

