from pathlib import Path
import shutil, send2trash

current_dir = Path.cwd()
downloads_dir = Path.home()/'Downloads'
# send2trash.send2trash('copy_test.py')
# send2trash.send2trash('helper_test.py')
# send2trash.send2trash('test_results.csv')

# moving all csv files from the downloads folder into the current dir

for csv_file in downloads_dir.iterdir():
    if csv_file.suffix == '.csv':
        destination = current_dir/csv_file.name
        shutil.copy(str(csv_file), str(destination))
        print(f'Copied {csv_file.name} into {current_dir}')