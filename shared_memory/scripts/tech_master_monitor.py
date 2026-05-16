import json, os, subprocess
def run_sandbox(code):
    with open("sandbox_log.txt", "a") as f: f.write(code)
