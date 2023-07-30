"""Modules"""
import subprocess
import sys


def execute_ebpf() -> bool:
    """
    Create a subprocess to invoke bootstrap, and time it out after 10s
    """
    output_file = open('ebpf-output.txt', mode='a', encoding='utf-8')
    try:
        results = subprocess.run(
            args=["./bootstrap"],
            stdout=output_file,
            stderr=subprocess.STDOUT,
            shell=True,
            check=False,
            text=True,
            timeout=10
        )
    except subprocess.TimeoutExpired:
        output_file.close()
        return True
    output_file.close()
    if results.returncode == 0:
        return True
    return False


if __name__ == "__main__":
    if execute_ebpf():
        sys.exit(0)
    sys.exit(1)
