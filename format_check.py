import argparse
import json

import pandas as pd

from detectors.detector import get_detector
from raid.detect import run_detection

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results_path", type=str, required=True, help="The path to the detection results JSON file")
    args = parser.parse_args()

    print(f"Checking format of {args.results_path}...")
    try:
        with open(args.results_path) as f:
            d = json.load(f)
    except json.decoder.JSONDecodeError:
        raise ValueError("Input is not a valid JSON file.\n") from None

    # Check if type is correct
    if type(d) != list:
        raise ValueError("Predictions are not of type list.\n")

    # Check if all elements have the correct fields
    if not all(['score' in elem and 'id' in elem for elem in d]):
        raise ValueError("Not all elements in your predictions have both 'id' and 'score' fields.\n")

    # Check for duplicate IDs
    if len([elem['id'] for elem in d]) != len(set([elem['id'] for elem in d])):
        raise ValueError("Found one or more duplicate 'id' fields. Please ensure each 'id' is unique.\n")
    
    
