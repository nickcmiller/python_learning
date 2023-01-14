import shutil
import os

current_directory = os.getcwd()
print(current_directory)

shutil.make_archive("lambda_handler", "zip", base_dir=".")
