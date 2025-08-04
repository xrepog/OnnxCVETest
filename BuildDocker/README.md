This onnxruntime test is under Triton server, testing the onnxruntime within the Triton

# Build your Triton container
docker build -t test-ort-triton .

# Run it with ports exposed
(Name the container with 'ort_test')  
docker run --name ort_test --rm -p8000:8000 test-ort-triton &

# See sth like below means start the triton server succefully
![image](running%20triton.png)

# Run shell script
## Get output data
sh ortTest.sh  
(The output data will store in result_ort.json)
## Convert the data to string
sh convert_data_toString.sh


# Triton API Defination
https://github.com/kserve/kserve/blob/master/docs/predict-api/v2/required_api.md















