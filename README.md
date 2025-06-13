# DuplicateFiles
********************************************************************************************************************************

**Notes:**

This method is reliable since it compares file content, not just name or size.

If you want to remove duplicates, you can modify the script to delete all but one from each group.

For very large folders, consider using SHA-1 or SHA-256 instead of MD5 for more accuracy (though MD5 is usually sufficient for duplicates).

********************************************************************************************************************************

**Summary of the Duplicate File Finder Script:**

The script scans a specified folder (including subfolders) to find duplicate files based on their content. Here's how it works:

Reads Files in Chunks: It uses the get_file_hash() function to read each file in binary mode and compute its MD5 hash (a unique fingerprint based on file content).

Builds a Hash Map: Files with the same hash are grouped together in a dictionary.

Identifies Duplicates: If multiple files share the same hash, they are considered duplicates.

Prints Results: For each set of duplicates, it prints their file paths and corresponding hash.

✅ This method ensures accuracy even if file names differ, as it compares actual file contents.

********************************************************************************************************************************

import os
import hashlib
from collections import defaultdict

def get_file_hash(file_path, chunk_size=4096):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return None
    return hasher.hexdigest()

def find_duplicates(folder_path):
    hash_map = defaultdict(list)
    
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_hash(file_path)
            if file_hash:
                hash_map[file_hash].append(file_path)
    
    # Filter only duplicates
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    
    return duplicates

# Example usage
folder = r"C:\Path\To\Your\Folder" #Place the Folder Path
duplicates = find_duplicates(folder)

if duplicates:
    print("🔍 Found duplicate files:")
    for hash_val, files in duplicates.items():
        print(f"\nDuplicate group (hash: {hash_val}):")
        for f in files:
            print(f"  {f}")
else:
    print("✅ No duplicates found.")
