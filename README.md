Autochat
========

A very simple script which will accept a file as an argument, 
and input each line of that file, in sequence, into any desired 
text field with focus. Useful for a very dumb but simple generic chat bot.

Installation
---

```sh
pip install -r requirements.txt
```

Usage
---

```sh
python autochat.py --help

usage: autochat.py [-h] [--period PERIOD] [--offset OFFSET] [--delay DELAY]
                   [--loglevel {DEBUG,INFO,WARN}]
                   script

positional arguments:
  script                File containing script to send one line at a time

optional arguments:
  -h, --help            show this help message and exit
  --period PERIOD       Time (in seconds) to wait between sending lines
  --offset OFFSET       Offset to this number of lines in the script
  --delay DELAY         Wait this long (in seconds) before sending the first
                        line
  --loglevel {DEBUG,INFO,WARN}
                        Set a desired log level
```