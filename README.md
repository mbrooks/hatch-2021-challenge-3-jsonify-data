# Hatch 2021 Challenge 3 Data Normalization Tools
The data for challenge 3 was delivered in some crazy format,
so I created some tools to convert it to JSON, which is
easier for computers to parse. The result is one JSON document
per line which represents a patient. The file itself is probably
not valid JSON, heh

JSON data can be found here:

    ./data/DomoArigatoData.json

## Install
If running locally install all of the required python packages

    pip install --no-cache-dir -r requirements.txt

## Usage
To JSONify data run the following:

    ./jsonify_data.py > data/DomoArigatoData.json

## Optional Commands
Fix file encoding and output results to ./data/DomoArigatoData-utf8.txt

    ./fix_encoding.py

To run the jsonify_data.py command, but in docker:

    ./docker-run.sh > data/DomoArigatoData.json

## Notes

* I had to fix a couple issues with the data by deleting one row
of data and fixing a character with another
* Yeah, I know it's still not valid JSON, but each row DOES contain a valid JSON doc.
* PRs are welcome, if you find a mistake