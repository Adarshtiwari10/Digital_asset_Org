# Digital Asset Organizer

A Python utility for automatically organizing files in a directory by extension or creation date.

## Features

- Organize files by extension or creation date
- Handles duplicate files automatically
- Generates detailed organization reports
- Supports all file types
- Clear console output showing progress
- Error handling for common issues

## Requirements

- Python 3.9 or higher
- No additional dependencies required

## Installation

1. Clone the repository
2. Navigate to the project directory

## Usage

Run the program using the command line with the following syntax:

```bash
python main.py --source <directory_path> --mode <organization_mode>
```

### Arguments

- `--source`: (Required) Path to the directory containing files to organize
- `--mode`: (Optional) Organization mode
  - `extension` (default) - Organizes files by their extension
  - `date` - Organizes files by creation date

### Examples

Organize by extension:
```bash
python main.py --source ~/Documents/unsorted
```

Organize by date:
```bash
python main.py --source ~/Documents/unsorted --mode date
```

## Output Structure

When organizing by extension:
```
source_directory/
└── organized_folders/
    ├── pdf/
    ├── jpg/
    ├── txt/
    ├── Others/
    └── organization_report.txt
```

When organizing by date:
```
source_directory/
└── organized_by_date/
    ├── 2023-07-06/
    ├── 2023-07-07/
    └── organization_report.txt
```

## Features in Detail

### File Categorization
- Files are sorted based on their extensions or creation dates
- Files without extensions are placed in an "Others" folder
- Duplicate files are handled by adding a number suffix

### Report Generation
- Creates a detailed report of the organization process
- Includes timestamp and file categorization details
- Saved as organization_report.txt in the output directory

## Error Handling

The program handles several common errors:
- Invalid directory paths
- Permission issues (especially on macOS)
- Duplicate file names
- Files without extensions

## Troubleshooting

### Permission Denied Error
On macOS, if you encounter permission issues:
1. Go to System Settings → Privacy & Security → Full Disk Access
2. Add Terminal or your code editor to grant access

## Project Structure

- main.py - Entry point of the application
- organizer
  - scanner.py - File discovery functionality
  - categorizer.py - File categorization logic
  - file_mover.py - File movement operations
  - reporter.py - Report generation
  - folder_creator.py - Output directory structure creation

## License

This projet is licensed under the [MIT license](LICENSE)

