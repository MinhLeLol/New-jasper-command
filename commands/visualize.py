#Full script is constructed by chat-gpt. I wrote the C codes that run as the sub-process
import subprocess
import os
import sys
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()


def get_c_dir():
    """
    Locate the Bit-masking-practice C project folder.
    Checks BITMASK_C_DIR, sibling folder, or default ~/Bit-masking-practice
    """
    env_dir = os.environ.get("BITMASK_C_DIR")
    if env_dir and os.path.exists(os.path.join(env_dir, "Makefile")):
        return os.path.abspath(os.path.expanduser(env_dir))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    sibling_dir = os.path.abspath(os.path.join(script_dir, "..", "Bit-masking-practice"))
    if os.path.exists(os.path.join(sibling_dir, "Makefile")):
        return sibling_dir

    default_dir = os.path.join(os.path.expanduser("~"), "Bit-masking-practice")
    if os.path.exists(os.path.join(default_dir, "Makefile")):
        return default_dir

    raise FileNotFoundError(
        "Makefile not found. Checked BITMASK_C_DIR, sibling, and default dirs."
    )

def build_c_program(c_dir):
    """Run make and return path to executable."""
    print(f"Building C project in: {c_dir}")
    subprocess.run(["make"], cwd=c_dir, check=True)

    exe_name = "mysolution.exe" if os.name == "nt" else "mysolution"
    c_program = os.path.join(c_dir, exe_name)
    if not os.path.exists(c_program):
        raise FileNotFoundError(f"C program not found at {c_program}")
    return c_program

def read_bits_file(bits_file_path):
    """Read the bits from the C program output file."""
    if not os.path.exists(bits_file_path):
        print(f"Error: {bits_file_path} not found.")
        return None
    with open(bits_file_path, "r") as f:
        return f.read().strip()

def display_bits(bits):
    """Display bits in a nice grid format."""
    count = len(bits)
    # Top border
    for i in range(count):
        print("┌─┐", end="")
        if (i + 1) % 4 == 0: print(" ", end="")
    print()
    # Bits row
    for i, bit in enumerate(bits):
        print(f"│{bit}│", end="")
        if (i + 1) % 4 == 0: print(" ", end="")
    print()
    # Bottom border
    for i in range(count):
        print("└─┘", end="")
        if (i + 1) % 4 == 0: print(" ", end="")
    print("\n")

def main(args):
    try:
        c_dir = get_c_dir()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    bits_file_path = os.path.join(c_dir, "bits_file.txt")

    while True:
        print("Press ENTER to continue, or type 'exit' to quit.")
        user_input = input("> ").strip().lower()
        if user_input in ["exit", "quit"]:
            print("Exiting...")
            break

        arg1 = input("Enter the number: ").strip()
        arg2 = input("Enter number of least significant bit: ").strip()

        # Build the C program before each run
        try:
            c_program = build_c_program(c_dir)
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            print(f"Error building C program: {e}")
            continue

        # Remove old output file
        if os.path.exists(bits_file_path):
            os.remove(bits_file_path)

        # Run the C program
        try:
            subprocess.run([c_program, arg1, arg2], cwd=c_dir, check=True)
        except subprocess.CalledProcessError:
            print("Error running C program.")
            continue

        # Read the generated text file
        bits = read_bits_file(bits_file_path)
        if bits is None:
            print("No bits were generated.")
            continue

        # Display bits
        display_bits(bits)
        time.sleep(0.2)

# Jasper CLI integration
def register(subparsers):
    parser = subparsers.add_parser(
        "visualize",
        help="Run bit visualization from the C program"
    )
    parser.set_defaults(func=main)
