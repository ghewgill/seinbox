import json
import subprocess
import sys

# hack to let this work with Python 2.6
if "check_output" not in dir(subprocess):
    def check_output(args):
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode != 0:
            raise subprocess.CalledProcessError(args)
        return out
    subprocess.check_output = check_output

inbox = json.loads(subprocess.check_output([sys.executable, "seinbox.py"]))
n = len(inbox["items"])
subprocess.call([sys.executable, "../ledbadge/message.py", str(n) if n else ""])
