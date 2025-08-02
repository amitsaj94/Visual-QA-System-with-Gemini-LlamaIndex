import os
from pathlib import Path


list_of_files = [
     "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
        ]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass


for file in list_of_files:
    file_path = Path(file)
    if file_path.exists():
        print(f"File {file} exists.")
    else:
        print(f"File {file} does not exist. Please check the path.")    

# This code checks if the files in the list exist in the current directory.
# If a file does not exist, it prompts the user to check the path.  
# The list of files includes Python scripts and a Jupyter notebook related to a QA system with PDF support.
# The code is designed to ensure that all necessary files are present before proceeding with further operations.


