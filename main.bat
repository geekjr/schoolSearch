# Wget crawl command
wget -r -p --html-extension -U --no-clobber Mozilla https://www.ncps-k12.org
# Python .toml creation
python3 getData.py
# Build index
stork --build toml.toml
# Upload indexed file to Blob
python3 upload.py