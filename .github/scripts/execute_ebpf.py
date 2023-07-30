"""Modules"""
import argparse
import subprocess
import sys


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
    output_fp = open(output_file, mode='a', encoding='utf-8')
    try:
        results = subprocess.run(
            args=["./bootstrap"],
            stdout=output_fp,
            stderr=subprocess.STDOUT,
            shell=True,
            check=False,
            text=True,
            timeout=10
        )
    except subprocess.TimeoutExpired:
        output_fp.close()
        return True
    output_fp.close()
    if results.returncode == 0:
        return True
    return False


if __name__ == "__main__":
    REQUESTED_OUTPUT_FILE = parse_args()
    if execute_ebpf(REQUESTED_OUTPUT_FILE):
        sys.exit(0)
    sys.exit(1)
