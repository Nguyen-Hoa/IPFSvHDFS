import subprocess
import os

class Meter(object):

    def __init__(self, port):
        self.port = port
        self.cmd = ['./wattsup', self.port, '-g', 'watts']
        self.file = None

    def start(self, filename):
        self.filename = filename
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        self.file = open(filename, 'a+')
        self.wattsup_process = subprocess.Popen(self.cmd, stdout=self.file, stderr=subprocess.STDOUT, close_fds=True)
        print(f'meter {self.port} started.')

    def cleanup(self):
        self.file.close()
        pid = int(self.wattsup_process.pid)
        self.wattsup_process.terminate()
        self.wattsup_process.wait()
        print(f'meter {self.port} closed.')

class Util(object):

    def __init__(self, pids):
        self.cmd = ['./util.sh', pids]
        self.file = None

    def start(self, filename):
        self.util_process = subprocess.Popen([*self.cmd, filename])
        print(f'util started.')

    def cleanup(self):
        pid = int(self.util_process.pid)
        self.util_process.terminate()
        self.util_process.wait()
        print(f'util closed.')



