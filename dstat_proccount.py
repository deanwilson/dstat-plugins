### Authority: dean.wilson@gmail.com

class dstat_plugin(dstat):
    """
    Dstat Display Process Count plugin
    Displays the number of processes on a machine
    """

    def __init__(self):
        self.name = 'procs'
        self.vars = ('total',)
        self.type = 'd'
        self.width = 5
        self.scale = 10

    def check(self):
        try:
            global subprocess
            import subprocess
        except:
            raise Exception, 'Module needs the subprocess module.'
        return True

    def extract(self):
        total = subprocess.Popen("ps -efwww | wc", shell=True, stdout=subprocess.PIPE).communicate()[0]
        self.val['total'] = int( total.split()[0] )
