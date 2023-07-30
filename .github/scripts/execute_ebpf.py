"""Modules"""
import argparse
import subprocess
import sys
import time


def parse_args() -> str:
    """
    Get the requested output file path
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file')
    args = parser.parse_args()
    return str(args.output_file)


def execute_ebpf(output_file: str) -> bool:
    """
    Create a subprocess to invoke bootstrap, and time it out after 10s
    """
    try:
        subprocess.run(
            args=["./bootstrap &"],
            shell=True,
            check=True,
            text=True,
        )
        time.sleep(1)
        subprocess.run(args=['whoami'], shell=True, check=True, text=True)
        time.sleep(1)
    except Exception: # pylint: disable=broad-exception-caught
        return False
    return True


if __name__ == "__main__":
    REQUESTED_OUTPUT_FILE = parse_args()
    if execute_ebpf(REQUESTED_OUTPUT_FILE):
        sys.exit(0)
    sys.exit(1)
