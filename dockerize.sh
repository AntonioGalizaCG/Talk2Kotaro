docker build -t talk-with-kotaro:latest .
docker save talk-with-kotaro:latest > ./talk-with-kotaro.tar
scp -r ./talk-with-kotaro.tar <your user>@<your server's IP>
