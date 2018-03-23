import requests
from config import agent_ip
from weixin_api.ops import *


for name, ip in agent_ip.items():
    message = ''
    nc_req = requests.get("%s/nc" % ip)
    if nc_req.status_code != 200:
        content = nc_req.json()
        for k,v in content.items():
            message += (name + ' ' + k + ' ' + v + "\n")
        send_text(agentid, str(message)
