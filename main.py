def main():
    print("Hello from repl-nix-workspace!")

import os

encryption_key = os.environ.get("ENCRYPTION_KEY")

if not encryption_key:
    raise ValueError("FATAL: ENCRYPTION_KEY is not set. Halting startup.")

if __name__ == "__main__":
    main()
