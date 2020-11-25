# sample_screen_scraper
sample_screen_scraper

Basic CLI usage instructions
```bash
# Setup requirements
pip install -r requirements.txt
# install mysql connector for the SQLAlchemy library
pip install pymysql
# Invoke search
python search.py
```

NOTE: You'll need to create a 'config.txt' file in the root directory and populate the values
```bash
[Default]
USER_AGENT = Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0
URL = https://foo.com
```