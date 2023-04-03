import os
import colorama
import json

IN_FILE = 'test_nn.py'

OUT_FILE = 'out.py'
TIME_FILE = 'time.json'
MEM_FILE = 'mem.json'

START_TIME_CMD = (
    'import time\n'
    'import json\n'
    'time_dict, prev_time = {}, time.time()\n'
    f'f_time = open({TIME_FILE!r},\'w\')\n'
)

START_MEM_CMD = (
    'import psutil\n'
    'mem_dict, prev_mem = {}, psutil.cpu_percent()\n'
    f'f_mem = open({MEM_FILE!r}, \'w\')\n'
)

READ_TIME_CMD = lambda line_n, prefix: (
    f'{prefix}time_dict[{line_n}] = time_dict.get({line_n},0) + time.time() - prev_time\n'
    f'{prefix}prev_time = time.time()\n'
)

READ_MEM_CMD = lambda line_n, prefix: (
    f'{prefix}mem_dict[{line_n}] = mem_dict.get({line_n},0) + psutil.cpu_percent() - prev_mem\n'
    f'{prefix}prev_time = psutil.cpu_percent()\n'
)

END_TIME_CMD = (
    '\njson.dump(time_dict, f_time)'
)

END_MEM_CMD = (
    '\njson.dump(mem_dict, f_mem)'
)

def v(filename):
    with open(filename) as f:
        lines = f.readlines()
    out_lines = []
    out_lines.append(START_TIME_CMD)
    #out_lines.append(START_MEM_CMD)
    for i,line in enumerate(lines):
        if not len(line):
            continue
        if not line.strip():
            continue
        if 'class' in line:
            out_lines.append(line)
            continue
        if line[-1] != '\n':
            line += '\n'
        prefix = ''
        pre_line = line
        j = i + 1
        if not (not line.strip() or line.strip()[-1] != ":"):
            pre_line = lines[j]
            while not pre_line.strip():
                j += 1
                pre_line = lines[j]
        for e in pre_line:
            if e.isspace():
                prefix += e
            else:
                break
        out_lines.append(line)
        if 'def' in line:
            out_lines.append(f'{prefix}global prev_time\n')
        out_lines.append(READ_TIME_CMD(i, prefix))
        #out_lines.append(READ_MEM_CMD(i, prefix))
    out_lines.append(READ_TIME_CMD(len(lines),''))
    #out_lines.append(READ_MEM_CMD(len(lines),''))
    out_lines.append(END_TIME_CMD)
    #out_lines.append(END_MEM_CMD)
    with open(OUT_FILE, 'w') as f:
        for line in out_lines:
            f.write(line)

v(IN_FILE)

os.system('python out.py')

with open(TIME_FILE) as f:
    timings = json.load(f)

with open(MEM_FILE) as f:
    memories = json.load(f)

m = max(timings.values())


print("TIME PROFILE")

with open(IN_FILE) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        t = timings.get(str(i),0)
        color = colorama.Fore.GREEN
        if t > m/4:
            color = colorama.Fore.YELLOW
        if t > m/2:
            color = colorama.Fore.RED
        print(f'{color}{line}{colorama.Style.RESET_ALL}',end='')

print()
# print()
# print()
# print('MEMORY PROFILE')

# m = max(memories.values())

# with open(IN_FILE) as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         t = memories.get(str(i),0)
#         color = colorama.Fore.GREEN
#         if t > m/4:
#             color = colorama.Fore.YELLOW
#         if t > m/2:
#             color = colorama.Fore.RED
#         print(f'{color}{line}{colorama.Style.RESET_ALL}',end='')