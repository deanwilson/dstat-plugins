### Authority: dean.wilson@gmail.com

class dstat_plugin(dstat):
    """
    Dstat Display Memcache Hit Count plugin
    Displays the number of Memcache "get_hits" and "get_misses"
    """

    def __init__(self):
        self.name  = 'Memcache Hits'
        self.nick  = ('Hit', 'Miss')
        self.vars  = ('get_hits', 'get_misses')
        self.type  = 'd'
        self.width = 6
        self.scale = 50

    def check(self):
        try:
            global memcache
            import memcache
        except:
            raise Exception, 'Module needs the memcache module.'
        return True

    def extract(self):
        mc = memcache.Client(['127.0.0.1:11211'], debug=0)
        stats = mc.get_stats()

        self.val['get_hits']   = int( stats[0][1]['get_hits'] )
        self.val['get_misses'] = int( stats[0][1]['get_misses'] )
