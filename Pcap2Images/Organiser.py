import os
import shutil
import time

# Define the source directory where the original images are stored
continousBufferFolderName = '/PLC_IMages_150/Continous'
FreshBufferFolderName = '/PLC_IMages_150/Fresh'
FinalBufferFolderName = '/PLC_IMages_150/Final'

FileLoc = 'C:/Users/callu/Documents/Python Scripts/Building/Pcap2Images'

DataPool = FileLoc + '/DataPool'
PLCPool =  FileLoc + '/PLC_POOL'

ladder = '/ladder'
plcDOS = '/DOS'
other = '/other'

BruteForceFolderName = '/Brute_Force_attack'
DecoyLogFolderName = '/Decoy_log'
InjectionAttackFolderName = '/Injection_attack'
PLCAttackFolderName = '/PLC_attack'
XSSAttackFolderName = '/XSS_attack'
Scans = '/Scans'

CommandInjectionFolderName = '/Command_Injection'
SqlInjectionFolderName = '/Sql_Injection'

XSSDOMFolderName = '/DOM'
XSSReflectedFolderName = '/Reflected'
XSSStoredFolderName = '/Stored'

FailFolderName = '/Fail'
PassFolderName = '/Pass'

EasyFolderName = '/Easy'
MediumFolderName = '/Medium'
HardFolderName = '/Hard'
ImpossibleFolderName = '/Impossible'

source_dir = FileLoc + FinalBufferFolderName + '/'

output_dir = ''

if continousBufferFolderName in source_dir:
    output_dir = PLCPool + '/Continous'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
elif FreshBufferFolderName in source_dir:
    output_dir = PLCPool + '/Fresh'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
elif FinalBufferFolderName in source_dir:
    output_dir = PLCPool + '/Final'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

start = time.time()

counter = 0
start = time.perf_counter()


# Loop through all the image files in the source directory
with os.scandir(source_dir) as entries:
    for entry in entries:
        output_path = output_dir
        filename = entry.name
        counter += 1
        if 'scans' in filename:
            output_path = f"{output_path}{other}"
        #elif 'decoy' in filename:
        #    output_path = output_path + DecoyLogFolderName
        else:
            if 'plc' in filename:
                if 'DOS' in filename:
                     output_path = f"{output_path}{plcDOS}"
                else:
                     output_path = f"{output_path}{ladder}"
            else:
                output_path = f"{output_path}{other}"
            #if 'sqli' in filename:
            #    output_path = f"{output_path}{InjectionAttackFolderName}{SqlInjectionFolderName}"
            #elif 'comsi' in filename or 'ci' in filename:
            #    output_path = f"{output_path}{InjectionAttackFolderName}{CommandInjectionFolderName}"
            #elif 'brute_force' in filename:
            #    output_path = f"{output_path}{BruteForceFolderName}"
            #elif 'plc' in filename:
            #    output_path = f"{output_path}{PLCAttackFolderName}"
            #elif 'xss' in filename:
            #    if 'dom' in filename:
            #        output_path = f"{output_path}{XSSAttackFolderName}{XSSDOMFolderName}"
            #    if 'reflected' in filename:
            #        output_path = f"{output_path}{XSSAttackFolderName}{XSSReflectedFolderName}"
            #    if 'stored' in filename:
            #        output_path = f"{output_path}{XSSAttackFolderName}{XSSStoredFolderName}"
            #if '_f' in filename or '_u' in filename:
            #    output_path = f"{output_path}{FailFolderName}"
            #elif '_p' in filename or '_s' in filename:
            #    output_path = f"{output_path}{PassFolderName}"
            #if 'easy' in filename:
            #    output_path = f"{output_path}{EasyFolderName}"
            #elif 'medium' in filename:
            #    output_path = f"{output_path}{MediumFolderName}"
            #elif 'hard' in filename:
            #    output_path = f"{output_path}{HardFolderName}"
            #elif 'impossible' in filename:
            #    output_path = f"{output_path}{ImpossibleFolderName}"
        if counter % 1000 == 0:
            elapsed = (time.perf_counter() - start)
            print(filename)
            print(output_path)
            print(f"Avg time per file: {elapsed:.2f} ms")
            start = time.perf_counter()
        filepath = os.path.join(source_dir, filename)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        if not os.path.exists(os.path.join(output_path, filename)):
            shutil.move(filepath, output_path)
        else:
            print(f"File '{filename}' already exists in '{output_path}', skipping...")
