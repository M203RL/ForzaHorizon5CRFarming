import ctypes
import sys
import subprocess
import pkg_resources

required = {'opencv-python', 'pynput', 'mss', 'screeninfo'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


def main():
    """
    Test function to run as admin
    """
    p = subprocess.Popen(
        'start cmd /c python Task.py',
        shell=1,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    p.communicate()
    return


def is_admin():
    """
    Determine whether the current script has admin privilege
    @return: bool. whether the script is in admin mode
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def rerun_as_admin():
    """
    Re-run the current python script as admin using the python interpreter
    from `sys.excutable`

    Note: it is difficult to get output at the original console.
    """
    ctypes.windll.shell32.ShellExecuteW(
        None,
        u"runas",
        str(sys.executable),
        str(__file__),
        None,
        1
    )


if __name__ == "__main__":
    if is_admin():
        main()
    else:
        rerun_as_admin()
