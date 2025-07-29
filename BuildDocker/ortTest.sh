# make new model directory
#docker exec -it ort_test mkdir -p /models/malicious_onnx/1

# copy model and config file into docker
#docker cp ./malicious_onnx/malicious.onnx ort_test:/models/malicious_onnx/1/model.onnx
#docker cp ./malicious_onnx/config.pbtxt ort_test:/models/malicious_onnx/config.pbtxt

#load malicious model
curl -X POST localhost:8000/v2/repository/models/malicious_onnx/load

curl -X POST localhost:8000/v2/models/malicious_onnx/infer   -H "Content-Type: application/json"   -d '{
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

