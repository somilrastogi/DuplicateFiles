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

