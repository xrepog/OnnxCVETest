# Build your Triton container
docker build -t test-ort-triton .

# Run it with ports exposed
docker run --rm -p8000:8000 -p8001:8001 -p8002:8002 test-ort-triton &
## See sth like below means start the triton server succefully
![image](running%20triton.png)
# Run shell script. 
## Using chmod to give permission before running.
./testORT.sh

















