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
            authstr += base64.b64encode('{0}:{1}'.format(authentication[0], authentication[0]).encode())
            self.headers['Authorization'] = authstr

basepath = '/home/markus/boxdispatcher/incoming'
        
targets = {Params
            (
                os.path.join(basepath,'olympia/Olympia.zip'),
                'http://35.189.126.113:1300',
                {
                    'content-type':'application/zip',
                    'player-datatype': 'hotelonly',
                    'player-msgtype':'Zip',
                    'player-brand':'OLYB2C',
                    'add-command':'erase' 
                },
                None
            ), #Entry for Travellanda test
         Params
           (
              os.path.join(basepath,'aircanada_travco/travco.zip'),
              'https://preprocess-proxy.acv-test.peakwork-platform.com',
              {
                'Player-Environment': 'Box',
                'Player-Brand': 'TRAVCO',
                'Player-DataType': 'HotelOnly',
                'Player-MsgType': 'Zip',
              }
              ('acv':'dvfas89uu3kjndfs78pas89m')
        }


class UploadParams(object):
    """Parameter object for uploading files to (s)ftp which proxies
    the boxes"""
    def __init__(self, localpath, filename, ftppath):
        self.zipfilename = zipfilename
        self.localpath = localpath
        self.filename = filename
        self.ftppath = ftppath
