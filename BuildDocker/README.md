This onnxruntime test is under Triton server, testing the onnxruntime within the Triton

# Build your Triton container
docker build -t test-ort-triton .

# Run it with ports exposed
(Name the container with 'ort_test') /n
docker run --name ort_test --rm -p8000:8000 test-ort-triton &

# See sth like below means start the triton server succefully
![image](running%20triton.png)

# Run shell script
(Using chmod to give permission before running) /n
./ortTest.sh


# Triton API Defination
https://github.com/kserve/kserve/blob/master/docs/predict-api/v2/required_api.md















