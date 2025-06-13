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
folder = r"G:\My Drive\My_Data\Sizing Calc 2.0\2025\ServiceNow\pdf_attachments\2025"
duplicates = find_duplicates(folder)

if duplicates:
    print("🔍 Found duplicate files:")
    for hash_val, files in duplicates.items():
        print(f"\nDuplicate group (hash: {hash_val}):")
        for f in files:
            print(f"  {f}")
else:
    print("✅ No duplicates found.")
