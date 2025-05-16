import os
def rename_files_sequentially(folder_path, extension):
    if not os.path.isdir(folder_path):
        print(f"The folder path '{folder_path}' is not valid.")
        return

    files = [f for f in os.listdir(folder_path) if f.lower().endswith(extension)]
    files.sort()
    for index, file in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file)
        new_filename = f"{index}{extension}"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_filename}'")

folder_path = 'cluttereadfolder'
extension = '.png'
rename_files_sequentially(folder_path, extension)

