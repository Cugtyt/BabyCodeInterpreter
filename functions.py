from IPython.terminal.interactiveshell import InteractiveShell
from IPython.utils import io

shell = InteractiveShell()

def execute_python_code(code, **kwargs):
    with io.capture_output() as captured:
        output = shell.run_cell(code)
    if output.success:
        return str(captured.stdout)
    else:
        return str(type(output.error_in_exec)) + ": " + str(output.error_in_exec)


def mail_paper_copy_to(file, to, mode="color", **kwargs):
    return "Mail file at: " + file + ", mode: " + mode + ", to: " + to + ", done."