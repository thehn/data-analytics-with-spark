import os
import subprocess

# Specify the directory
target_directory = "./notebook_data"

# Recursively find all .ipynb files in the specified directory
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(".ipynb"):
            notebook_path = os.path.join(root, file)
            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--ClearOutputPreprocessor.enabled=True",
                    "--inplace",
                    notebook_path,
                ]
            )
