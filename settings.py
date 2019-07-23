import base64
import os

class Params(object):
    """group parameters required for dispatching files to a 
    box environment"""
    def __init__(self, zipfilename, url, headers, authentication = None):
        self.zipfilename = zipfilename
        self.url = url
        self.headers = headers
        if authentication is not None:
            authstr = b'Basic '
            authstr += base64.b64encode('{0}:{1}'.format('Hotelplan', '627257').encode())
            self.headers['Authorization'] = authstr

basepath = '/home/markusbarth/webapps/boxdispatcher/incoming'
        
targets = {Params
            (
                os.path.join(basepath,'olympia/Olympia.zip'),
                'http://35.204.76.157:1300',
                {
                    'content-type':'application/zip',
                    'player-datatype': 'hotelonly',
                    'player-msgtype':'Zip',
                    'player-brand':'OLY',
                    'add-command':'erase' 
                },
                (
                    'Hotelplan',
                    '627257'
                )
            ),
          Params
            (
                os.path.join(basepath,'tui_brintest/cleartrip.zip'),
                'http://35.193.196.136:1300',
                {
                    'content-type':'application/zip',
                    'player-datatype': 'hotelonly',
                    'player-msgtype':'Zip',
                    'player-brand':'CLEARTRIP',
                    'add-command':'erase' 
                },
                None
            ),
          Params
            (
                os.path.join(basepath,'tui_brintest/toureast.zip'),
                'http://35.193.196.136:1300',
                {
                    'content-type':'application/zip',
                    'player-datatype': 'hotelonly',
                    'player-msgtype':'Zip',
                    'player-brand':'TOUREAST',
                    'add-command':'erase' 
                },
                None
            )
        }


class UploadParams(object):
    """Parameter object for uploading files to (s)ftp which proxies
    the boxes"""
    def __init__(self, localpath, filename, ftppath):
        self.zipfilename = zipfilename
        self.localpath = localpath
        self.filename = filename
        self.ftppath = ftppath
