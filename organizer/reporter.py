from datetime import datetime
from pathlib import Path

def generate_report(categorized, output_folder):
    report_lines = []
    timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    report_lines.append(f"Report Generated on: {timestamp}\n")

    for ext, files in categorized.items():
        report_lines.append(f"\nOrganized into folder: {ext}")
        for file in files:
            report_lines.append(f" -- {file.name}")
    
    report_text = "\n".join(report_lines)

    report_file = output_folder / "organization_report.txt" #to written a csv file use .csv extension
    with open (report_file, "w") as f:
        f.write(report_text)
    print(f"Report is written to {report_file}")

    