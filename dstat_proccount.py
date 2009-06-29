### Dstat Display Process Count plugin
### Displays the number of processes on a machine
###
### Authority: dean.wilson@gmail.com

class dstat_proccount(dstat):
    def __init__(self):
        self.name   = 'Tot Procs'
        self.format = ('d', 8, 100)
        self.nick   = ('num procs',)
        self.vars   = ('procs',)

        self.init(self.vars, 1)

    def check(self):
        try:
            global subprocess
            import subprocess
        except:
            raise Exception, 'Module needs the subprocess module.'
        return True

    def extract(self):
        total = subprocess.Popen("ps -efwww | wc", shell=True, stdout=subprocess.PIPE).communicate()[0]
        self.val['procs'] = int( total.split()[0] )
