import os
import re
import sys

def verify_html(file_path):
    if not os.path.exists(file_path):
        print(f"Error: HTML file not found at: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []

    # Search for XX%, XX, YY, ZZ, 06-XX placeholders
    placeholders = re.findall(r'\b[XYZ]{2,}\b|\bXX\b|\bYY\b|\bZZ\b|06-XX', content)
    if placeholders:
        errors.append(f"Found unpopulated placeholders: {set(placeholders)}")

    # Search for template instructions
    if "<!-- 在此处插入当日所有的 match-card -->" in content:
        errors.append("Template placeholder comment still exists.")

    if len(errors) == 0:
        print(f"Verification SUCCESS: {file_path} is clean and ready!")
        return True
    else:
        print(f"Verification FAILED for {file_path}:")
        for err in errors:
            print(f"  - {err}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 verify_matchday_html.py <html_file_path>")
        sys.exit(1)
        
    path = sys.argv[1]
    success = verify_html(path)
    sys.exit(0 if success else 1)
