import subprocess

def rofi(prompt, options, rofi_args=[], fuzzy=True):
    optionstr = '\n'.join(option.replace('\n', ' ') for option in options)
    args = ['rofi', '-sort', '-no-levenshtein-sort']
    if fuzzy:
        args += ['-matching', 'fuzzy']
    args += ['-dmenu', '-p', prompt, '-format', 's', '-i', '-lines', '5']
    args += rofi_args
    args = [str(arg) for arg in args]


    result = subprocess.run(args, input=optionstr, stdout=subprocess.PIPE, universal_newlines=True)
    returncode = result.returncode
    stdout = result.stdout.strip()

    selected = stdout.strip()
    try:
        index = [opt.strip() for opt in options].index(selected)
    except ValueError:
        index = -1

    if returncode == 0:
        key = 0
    elif returncode == 1:
        key = -1
    elif returncode > 9:
        key = returncode - 9

    return key, index, selected
