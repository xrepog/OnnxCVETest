# copy the python script and json into docker
chmod +x ort_output.sh
./ort_output.sh
docker cp ./ortProfExploit.py ort_test:/models/ortProfExploit.py
docker cp ./result_ort.json ort_test:/models/result_ort.json

# run python script
docker exec -it ort_test bash -c "python3 /models/ortProfExploit.py"

