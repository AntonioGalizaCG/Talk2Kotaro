docker build -t talk-with-kotaro:latest .
docker save talk-with-kotaro:latest > ./talk-with-kotaro.tar
scp -r ./talk-with-kotaro.tar antonio@mizuuchi2.lab.tuat.ac.jp:talk-with-kotaro.tar
