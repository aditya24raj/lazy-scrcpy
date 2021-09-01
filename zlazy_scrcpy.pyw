from json import load
from subprocess import Popen, PIPE, CREATE_NO_WINDOW


path_scrcpy = r"scrcpy-noconsole.exe"
path_config_file = "config.json"


def show_error(this_error):
    remark = r"\nPress any to exit..."
    with Popen(f"""python -c "input('{this_error + remark}')" """) as _:
        pass


def get_android_id():
    get_android_id_command = "adb shell settings get secure android_id"

    with Popen(
            get_android_id_command,
            stdout=PIPE, stderr=PIPE,
            creationflags=CREATE_NO_WINDOW
    ) as get_android_id_subprocess:
        android_id = get_android_id_subprocess.stdout.read().decode().strip()

        if android_id:
            return android_id
        else:
            show_error(
                get_android_id_subprocess.stderr.read().decode().strip()
            )


def start_scrcpy_for_this_id(android_id):
    global path_config_file
    global path_scrcpy

    with open(path_config_file) as config:
        config_data_json = load(config)
    
    scrcpy_arguments = config_data_json[android_id] if android_id in config_data_json else config_data_json["default"]
    with Popen(f"{path_scrcpy} {scrcpy_arguments}", stderr=PIPE) as scrcpy_subprocess:
        scrcpy_subprocess_error = scrcpy_subprocess.stderr.read().decode().strip()
        if scrcpy_subprocess_error:
            show_error(scrcpy_subprocess_error)

start_scrcpy_for_this_id(get_android_id())
