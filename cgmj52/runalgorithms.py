import subprocess
import os

input_file_names = ["AISearchfile026.txt", "AISearchfile042.txt",
                    "AISearchfile048.txt", "AISearchfile058.txt", "AISearchfile175.txt", "AISearchfile180.txt", "AISearchfile535.txt"]
programs = ["AlgBbasic.py"
            ]
os.chdir('cgmj52')
current_working_directory = os.getcwd()

file_list = os.listdir(current_working_directory)

for file in file_list:
    if os.path.isfile(os.path.join(current_working_directory, file)):
        print(file)
for i in input_file_names:
    for j in programs:
        subprocess.run(['python', j, i])
