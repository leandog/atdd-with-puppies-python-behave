import os
import subprocess
from datetime import datetime


def execute_features():
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, 'test_execution_reports')
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
    htmlpath = 'test_execution_reports' + '\\' + 'Test_Automation_Report_' \
               + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

    command = ["behave", "-f", "html-pretty", "-o", htmlpath]

    subprocess.run(command, check=True)
    print("Test cases are executed successfully. The report will be available at " + htmlpath)


if __name__ == '__main__':
    execute_features()
