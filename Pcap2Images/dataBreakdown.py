import os
import matplotlib.pyplot as plt 

def count_files(dir_path):
    """
    Recursively count the number of files in a directory and its subdirectories.
    """
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            file_count += 1
    return file_count

def list_subdirectories(dir_path):
    """
    Recursively list all subdirectories in a directory and its subdirectories.
    """
    subdirectories = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for dirname in dirnames:
            subdirectories.append(os.path.join(dirpath, dirname))
    return subdirectories

def create_pie_chart(dir_path, file):
    """
    Recursively create pie charts for each subdirectory that has subdirectories
    """
    sub_dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    if len(sub_dirs) > 0:
        sub_dir_counts = []
        sub_dir_names = []
        for sub_dir in sub_dirs:
            sub_dir_path = os.path.join(dir_path, sub_dir)
            sub_dir_count = count_files(sub_dir_path)
            if sub_dir_count > 0:
                sub_dir_counts.append(sub_dir_count)
                sub_dir_names.append(f'{sub_dir} ({sub_dir_count})')
                file.write(f"{sub_dir}: {sub_dir_count}\n")
                print(f"{sub_dir}: {sub_dir_count}\n")
        # Commented out pie chart
        if len(sub_dir_counts) > 0:
             plt.pie(sub_dir_counts, labels=sub_dir_names, autopct='%1.1f%%')
             plt.title(f'Distribution of files in {dir_path}')
             plt.legend(bbox_to_anchor=(1.2, 0.5))
             plt.show()
             for sub_dir in sub_dirs:
                    sub_dir_path = os.path.join(dir_path, sub_dir)
                    create_pie_chart(sub_dir_path, file)

# Define the root directory where the files are stored
root_dir = 'C:/Users/callu/Documents/Python Scripts/Building/Pcap2Images/Datasets/DecoyDatasetv8'

# Create pie chart for the top-level directories
with open("categories.txt", "w") as file:
    create_pie_chart(root_dir, file)

# Check for unbalanced pie charts
unbalanced_charts = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if len(dirnames) == 0:
        continue
    for dirname in dirnames:
        dir_path = os.path.join(dirpath, dirname)
        sub_dirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
        if len(sub_dirs) > 1:
            sub_dir_counts = []
            for sub_dir in sub_dirs:
                sub_dir_path = os.path.join(dir_path, sub_dir)
                sub_dir_count = count_files(sub_dir_path)
                sub_dir_counts.append(sub_dir_count)
            total_files = sum(sub_dir_counts)
            for count in sub_dir_counts:
                if total_files > 0:
                    if count / total_files > 0.8:
                        unbalanced_charts.append(dir_path)
                        break;
                else:
                    unbalanced_charts.append(dir_path)
                    break;

if len(unbalanced_charts) > 0:
    print('The following directories have unbalanced pie charts:')
    for chart in unbalanced_charts:
        print(chart)
else:
    print('All pie charts are balanced')
