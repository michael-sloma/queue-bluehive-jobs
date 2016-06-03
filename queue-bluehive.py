import sys
import os
import time

max_queue_size, jobdir = sys.argv[1:]
max_queue_size = int(max_queue_size)
username = os.popen("echo $USER").read()

remaining_jobs = os.listdir(jobdir)

def run_command(cmd):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.stdout

def get_current_queue_size():
    queue = run_command("squeue -u %s" % username)
    return len(queue.split("\n"))

def run_job(jobname):
    run_command("sbatch %s" % jobname)

while True:
    qdiff = max_queue_size - get_current_queue_size()
    for _ in range(qdiff):
        if len(remaining_jobs)==0:
            break
        run_job(remaining_jobs.pop())
    time.sleep(10)
