import argparse

parser = argparse.ArgumentParser(description="A script that greets the user.")
parser.add_argument("name", help="The name of the user")
args = parser.parse_args()

print(f"Hello, {args.name}!")
