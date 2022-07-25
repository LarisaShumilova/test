#!/usr/bin/python3
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file', required=True)

args = parser.parse_args()

with open(args.file) as f_orig_json:
    json_text = f_orig_json.read()

    try:
        pretty_json = json.dumps(json.loads(json_text), indent=2)

        if json_text != pretty_json:
            with open(args.file, "w") as f_form_json:
                f_form_json.write(pretty_json)

    except Exception as e:
        print('Error:')
        print(e)

