This repo is the proof of exploit for onnxruntime CVE
Exploit is under Triton server, testing the onnxruntime within the Triton

# Build Docker
docker build -t test-ort-triton .

# Run it with ports exposed
(Name the container with 'ort_test')  
docker run --name ort_test --rm -p8000:8000 test-ort-triton &

## See sth like below means start the triton server succefully
![image](running%20triton.png)

# Run python script
(Assuming python is installed)
python/python3 ortProfExploit.py

# Triton API Defination
The API of triton server is needed to exploit onnxruntime platform integrated in triton.  
Below is the link of how nvidia define the api of triton   
https://github.com/kserve/kserve/blob/master/docs/predict-api/v2/required_api.md















