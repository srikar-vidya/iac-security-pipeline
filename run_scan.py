import subprocess
import sys

print("🔍 Running Checkov Scan...")
result = subprocess.run(["checkov", "-d", "."], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)

if result.returncode != 0:
    print("❌ Issues found. Failing build.")
    sys.exit(1)
else:
    print("✅ No issues found. Build passes.")
