# Setup venv.
python3 -m venv ./venv
./venv/bin/pip3 install -r requirements.txt

# Install chrome driver.
cd ./venv/bin
wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
