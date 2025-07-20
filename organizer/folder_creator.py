from pathlib import Path

def create_categorized_structure(categorized, base_path):
    organized_dir = base_path / "organized_folders"
    organized_dir.mkdir(exist_ok=True)

    for ext in categorized:
        ext_folder = organized_dir / ext
        ext_folder.mkdir(exist_ok=True)
    
    return organized_dir  