# Build your Triton container
docker build -t dockerfile .

# Run it with ports exposed
docker run --rm -p8000:8000 -p8001:8001 -p8002:8002 my-triton

# Run shell script. Using chmod to give permission before running.
./testORT.sh

















