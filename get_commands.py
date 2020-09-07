def fetch_commands(file):
    with open(file) as cmd_file:
        commands = cmd_file.read().split('\n')
    return commands