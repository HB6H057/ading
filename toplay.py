# -*- encoding: utf-8 -*-
# Author: HB6H057<e@hb6.org>
#         http://www.hb6.org
# Created on 2015-03-01

import sys
from optparse import OptionParser  


parser = OptionParser()  
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE") 
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout")
(options, args) = parser.parse_args() 


def __name__ == '__main__':

    print "Hello World"