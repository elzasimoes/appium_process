import psutil
import subprocess
import time

def start_appium_server(port, log_file):
    command = [
        'appium',
        '-p', str(port), 
        '--log', log_file # Arquivo de log para saída do Appium
    ]
    
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def find_pid_by_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            pid = conn.pid
            return pid
    return None

def close_process(pid):
    process = psutil.Process(pid)
    process.terminate()
    process.wait()


port = 4725
start_appium_server(port, 'appium_{0}.log'.format(port))
time.sleep(15)
pid = find_pid_by_port(port)
close_process(pid)
