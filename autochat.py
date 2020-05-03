import pyautogui
import argparse
import logging
import time

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=str, help="File containing script to send one line at a time")
    parser.add_argument("--period", type=int, help="Time (in seconds) to wait between sending lines", default=60)
    parser.add_argument("--offset", type=int, help="Offset to this number of lines in the script", default=0)
    parser.add_argument("--delay", type=int, help="Wait this long (in seconds) before sending the first line", default=0)
    parser.add_argument("--loglevel", type=str, help="Set a desired log level", choices=['DEBUG', 'INFO', 'WARN'], default=None)

    args = parser.parse_args()

    # Setup a basic logger, or disable it if none was requested.
    if args.loglevel is None:
        logging.disable(logging.CRITICAL)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=args.loglevel)

    with open(args.script, "r") as script:
        lines = script.readlines()

    # Strip whitespace/control characters from each line, and remove blank ones.
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

    logging.info("Parsed {} lines".format(len(lines)))

    time.sleep(args.delay)

    logging.debug("Begin autochat...")
    for line in lines[args.offset:]:
        logging.debug("Sending {}".format(line))
        pyautogui.write(line)
        pyautogui.press("enter")
        time.sleep(args.period)

    logging.info("Script complete")