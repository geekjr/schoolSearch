# Wget crawl command
cd ~/crawling
wget -r -p --html-extension -U --no-clobber Mozilla https://www.ncps-k12.org
cd ..
# Python .toml creation
python3 getData.py
# Build index
./stork-ubuntu-latest --build toml.toml
# Upload intexed file to Blob
python3 upload.py
# Make a backup of the crawled data
zip -r www.ncps-k12.org.zip ~/crawling/www.ncps-k12.org
python3 backup.py
rm -r www.ncps-k12.org.zip