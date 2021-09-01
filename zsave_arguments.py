from subprocess import Popen, PIPE, CREATE_NO_WINDOW
from json import load, dump

def get_android_model():
    with Popen(
        "adb shell getprop ro.product.model",
        stdout=PIPE,
        creationflags=CREATE_NO_WINDOW) as get_android_model_subprocess:
        return get_android_model_subprocess.stdout.read().decode().strip()
        

def get_android_id():
    get_android_id_command = "adb shell settings get secure android_id"

    with Popen(
            get_android_id_command,
            stdout=PIPE, stderr=PIPE,
            creationflags=CREATE_NO_WINDOW
    ) as get_android_id_subprocess:
        android_id = get_android_id_subprocess.stdout.read().decode().strip()

        if android_id:
            print(f"\nConnected to: {get_android_model()}")
            return android_id
        else:
            print(get_android_id_subprocess.stderr.read().decode().strip())
            if input("Do you want to modify default arguments? [y/n, default=n]: ") == "y":
                return "default"


def get_new_arguments():
    print("\nEnter arguments for scrcpy-")
    return input("scrcpy ")


def modify_arguments(android_id, arguments):
    config_data = []

    with open("config.json") as config_file:
        config_data = load(config_file)

    with open("config.json", "w") as config_file:
        config_data[android_id] = arguments
        dump(config_data, config_file, ensure_ascii=False, indent=4)
    
    print("\nSaved all arguments. ")


if __name__=="__main__":
    modify_arguments(android_id=get_android_id(), arguments=get_new_arguments())
    print("Launch using start_scrcpy.py for these arguments to be auto-applied.")
    input("Press enter to exit..")

