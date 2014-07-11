**Analyzes EZproxy-generated log files and spits out a CSV with this info:**

This is a fork of https://github.com/robincamille/ezproxy-analysis. made as standalone because of some differences in our orgs ezproxy set up.

* Filename of log being analyzed
* # total connections
* # on-campus connections (as determined by IP addresses starting with "10." -- may be different for your campus)
* % on-campus connections of total
* # off-campus connections
* % off-campus connections of total
* # library connections (as determined by IP addresses starting with "10.11" and "10.12" -- will almost certainly be different for your campus)
* % library of on-campus connections
* % library of total connections
* # student sessions off-campus
* % student sessions of total off-campus
* # fac/staff sessions off-campus
* % fac/staff sessions of total off-campus

Use it on the command line like so: 

**python ezp-analysis.py [directory to analyze -- should be SPU logs] [desired output filename.csv]**


## Please note

* "Sessions" are different from "connections." Sessions are when someone logs into EZproxy and does several things; a connection is a single HTTP request. Sessions can only be tracked if they're off-campus, as they rely on a session ID. On-campus EZproxy use doesn't get a session ID and so can only be tracked with connections, which are less useful. On-campus use doesn't tell us anything about student vs. faculty use, for instance.
* Make sure to change the IP address specifications within the script. As it is, it counts "on campus" as IP addresses beginning with "10." and in-library as beginning with "10.11." or "10.12."
* This is a pretty hacky script. I make no guarantees as to the accuracy of this script. Go over it with a fine-toothed comb and make sure your output lines up with what you see in your other data sources.
* This output is only a sketch of how EZproxy may be used on your campus.
* Please take a good look at the logs you're analyzing and familiarize yourself with them — otherwise you may get the wrong idea about this script's output!
