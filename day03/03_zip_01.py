import zipfile
import os

RESULT_DIR = 'rss_results'

zip_flle = zipfile.ZipFile('results.zip', 'w')

for root, dirs, files in os.walk(RESULT_DIR):
    for file in files:
        zip_flle.write(os.path.join(root, file))

zip_flle.close()