
import subprocess
import os

venv_path = r"C:\Users\Lynn Lin\PycharmProjects\System_Testing_REST_API\.venv"
activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
pytest_executable = os.path.join(venv_path, "Scripts", "pytest.exe")

# Change directory to starter_code before running pytest
project_root = r"C:\Users\Lynn Lin\PycharmProjects\System_Testing_REST_API"
starter_code_path = os.path.join(project_root, "starter_code")

test_path = "tests\\system\\item_test.py::ItemTest::test_get_item_not_found"

# Set PYTHONPATH to include the starter_code directory
pythonpath = starter_code_path

install_command = f'call "{activate_script}" && pip install flask_jwt_extended'
subprocess.run(install_command, shell=True, capture_output=True, text=True)
command = f'call "{activate_script}" && cd /d "{starter_code_path}" && set PYTHONPATH={pythonpath} && "{pytest_executable}" {test_path}'

print(f"Executing command: {command}")
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("Stdout:")
print(result.stdout)
print("Stderr:")
print(result.stderr)
print("Exit Code:", result.returncode)
