#!/usr/bin/env python3
import urllib.request
from settings import targets
import logging
import os

logfolder = '/home/markus/boxdispatcher'
logging.basicConfig(filename=os.path.join(logfolder,'dispatch.log'),
                    level=logging.INFO
                    )

class Dispatcher(object):
    def __init__(self, targets):
        self.targets = targets
    def run(self):
        for target in self.targets:
            try:
                f = open(target.zipfilename,'rb')
                data = f.read()
            except IOError:
                pass
            else:
                rq = urllib.request.Request(target.url, data, headers=target.headers)
                try:
                    rs = urllib.request.urlopen(rq)
                except urllib.error.HTTPError as e:
                    logging.error("HTTPError")
                    logging.error(e.read())
                    logging.error(e.code)
                    logging.error(e.reason)
                    logging.error(e.headers)
                else:
                    logging.info(rs.getcode())
                    logging.info(rs.info())
                    logging.info(rs.read().decode('utf-8'))
                    try:
                        os.remove(target.zipfilename)
                    except OSError:
                        pass


if __name__ == '__main__':
    dispatcher = Dispatcher(targets)
    dispatcher.run()
