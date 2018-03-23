import commands as cmd
from conf import SER_DICT

TIMEOUT = 1


class HttpGet(object):

    def nc(self):
        content = {}
        for k,v in SER_DICT.items():
            t = v.get('timeout', TIMEOUT)
            nc = 'nc -v -z -w %s %s %s' % (t, v['host'], v['port'])
            st,out = cmd.getstatusoutput(nc)
            if st != 0:
                content[k] = out
        return content


