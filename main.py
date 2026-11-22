#!/usr/bin/env python3
import os
import sys

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    src = "entry.png"
    dst = os.path.join(out_dir, "entry.png")
    
    if not os.path.exists(src):
        print(f"Error: {src} not found.", file=sys.stderr)
        sys.exit(1)
        
    with open(src, "rb") as f_in:
        data = f_in.read()
        
    with open(dst, "wb") as f_out:
        f_out.write(data)
        
    print(f"Successfully copied {src} ({len(data)} bytes) to {dst}")

if __name__ == "__main__":
    main()
