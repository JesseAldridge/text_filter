Apply a filter to some text.
===

Install
---
git clone git@github.com:JesseAldridge/text_filter.git
cd text_filter
pip install -r requirements.txt
ln -s $(PWD)/text_filter.py /usr/local/bin/tf

Run
---
1. Copy some text to your clipboard
2. Run `tf <filter_name>` (e.g. `tf normal_words`)
3. Your filtered text will be output to the console
