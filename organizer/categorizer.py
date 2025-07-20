from pathlib import Path
from datetime import datetime

def categorize_by_extension(files):
    categorized_files = {}
    for file in files:
        print(f"📄 Processing: {file.name}")
        ext = file.suffix.lower().lstrip('.') #get file extension
        print(f"extracted extension is {ext}")
        if not ext:
            ext = 'Others' #handle files with no extensions
        if ext not in categorized_files:
            categorized_files[ext] = []
        categorized_files[ext].append(file)
    print(categorized_files)
    return categorized_files

#categorizing by date of creation
def categorize_by_date(files):
    categorized ={}
    for file in files:
        created_at = datetime.fromtimestamp(file.stat().st_ctime)
        date_str = created_at.strftime("%Y-%m-%d")
        if date_str not in categorized:
            categorized[date_str]=[]
        categorized[date_str].append(file)
    return categorized