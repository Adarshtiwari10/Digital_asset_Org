from pathlib import Path
from organizer.scanner import get_files_in_directory
from organizer.file_mover import move_files_by_category
from organizer.reporter import generate_report
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Digital Asset Organizer")
    parser.add_argument('--source', type=str, required=True,
                        help='Path to the folder to organize')
    parser.add_argument('--mode', type=str, choices=['extension','date'],default='extension',
                        help= 'Organized by "Extension"(default) or by "Date"')
    return parser.parse_args()

def main():
    args = parse_args()
    directory_path = Path(args.source)   
    try:
        files = get_files_in_directory(directory_path)
        if args.mode == "extension":
            from organizer.categorizer import categorize_by_extension
            categorized = categorize_by_extension(files)
            organized_dir = directory_path / "organized_folders"
        else:
            from organizer.categorizer import categorize_by_date
            categorized = categorize_by_date(files)
            organized_dir = directory_path / "organized_by_date"
        move_files_by_category(categorized, Path(organized_dir))
        # organized_dir = Path(directory_path) / "organized_folders"
        generate_report(categorized, organized_dir)
        for ext, group in categorized.items():
            print(f"{ext.upper()}: {len(group)}file(s)")
        print(f" Above are the Files & their count in '{directory_path}':")
        for file in files:
             print(file.name)
    except ValueError as e:
        print(e)
    except PermissionError as e:
        print("Permission denied while accessing the directory.")
        print("🔒 On macOS, go to System Settings → Privacy & Security → Full Disk Access.")
        print("   Add Terminal or your code editor to grant access.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
