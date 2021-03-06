import os
from bs4 import BeautifulSoup
import codecs

toml = open("toml.toml", "a")
toml.write("[input]\nbase_directory = './www.ncps-k12.org' \nurl_prefix = 'https://www.ncps-k12.org/' \nfiles = [")

for file in os.listdir("./www.ncps-k12.org/Page"):
    if file.endswith(".html"):
        try:
            pageNumber = str(file).split(".")[0]
            url = f"Page/{pageNumber}"
            f = codecs.open(
                '/home/azureuser/crawling/www.ncps-k12.org/Page/' + file, "r")
            parsed_html = BeautifulSoup(f.read(), features="html.parser")
            title = parsed_html.find(
                'title').text
            print("{path = '" + str('Page/'+file) + "', url = '" +
                  str(url) + "', title = '" + str(title) + "'},")
            toml.write("\n{path = '" + str('Page/' + file) + "', url = '" +
                       str(url) + "', title = '" + str(title).replace('"', '').replace("'", '') + "'},")
        except:
            continue

toml.write("\n]\n[output]\nfilename = 'school.st'")
toml.close()
