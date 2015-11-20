# Dstat Plugins #

> dstat - versatile tool for generating system resource statistics

> -- From the Debian dstat manpage

## Deprecation - 2015/11/20 ##

There are now plugins equivalent to the ones in this repo
inside dstat itself and so these should be considered deprecated.

## Intro ##

Sometimes you need resource statistics from a source that the original
author didn't include in dstat. This git repo contains some of mine.

The simplest way to use them is to drop the .py file in to ~/.dstat and
then run dstat with the -M filename option.

Example - 

    mkdir ~/.dstat
    cp ~/dstat_proccount.py ~/.dstat
    dstat -a -M proccount


## Plugins ##

### proccount ###

Shows the total number of current processes.

    $ dstat --proccount
    procs
    total
      286
      286

### memcache_hits ###

Shows the total "get" hits and misses. This is an absolute number, not
an incremental difference between runs.

    $ dstat --memcache-hits

### Author ###

[Dean Wilson](http://www.unixdaemon.net)
