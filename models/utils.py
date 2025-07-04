from natsort import natsorted
from glob import glob
import json

def dict_to_string(dct):
    # For logging purposes
    ret = ""
    for k, v in dct.items():
        ret += f"| {k}: {v}"
    return ret


def find_model(save_path):
    # By the syntax the outputted models, the last one in the list is the latest
    models = natsorted(list(glob(f"{save_path}/*.pth")))
    print(models, save_path)
    for m in models:
        if "best" in m:
            print("returning ", m)
            return m
        print(m)
    chosen = m
    return chosen

def log_metrics_json(metrics, log_file="logs/log.log"):
    with open(log_file, "a") as fd:
        fd.write(json.dumps(metrics) + ",\n")
