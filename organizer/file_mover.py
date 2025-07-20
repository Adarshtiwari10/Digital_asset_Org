import shutil

def move_files_by_category(categorized, base_path):
    for category, files in categorized.items():
        category_folder = base_path / category
        category_folder.mkdir(parents=True, exist_ok=True)

        for file in files:
            dest_path = category_folder / file.name

            # Handle duplicates
            counter = 1
            while dest_path.exists():
                new_name = f"{file.stem} ({counter}){file.suffix}"
                dest_path = category_folder / new_name
                counter += 1

            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name} → {category}/")
