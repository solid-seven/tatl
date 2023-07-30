"""Modules"""
import subprocess
import sys


def execute_ebpf() -> bool:
    """
    Create a subprocess to invoke bootstrap, and time it out after 10s
    """
    try:
        with open("$GITHUB_WORKSPACE/ebpf-output.log", encoding='utf-8') as output_file:
            results = subprocess.run(
                args=["./bootstrap"],
                stdout=output_file,
                check=False,
                timeout=10
            )
    except subprocess.TimeoutExpired:
        return True
    if results.returncode == 0:
        return True
    return False


if __name__ == "__main__":
    if execute_ebpf():
        sys.exit(0)
    sys.exit(1)
