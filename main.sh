# Wget crawl command
wget -r -p --html-extension -U --no-clobber Mozilla https://www.ncps-k12.org
# Python .toml creation
python getData.py
# Build index
./stork-ubuntu-latest --build toml.toml
# Upload intexed file to Blob
python upload.py
# Make a backup of the crawled data
zip -r www.ncps-k12.org.zip ~/crawling/www.ncps-k12.org
python backup.py
rm -r www.ncps-k12.org.zip