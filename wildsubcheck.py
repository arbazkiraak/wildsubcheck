#!/usr/bin/python3
###! optional:save it under /bin/
###! use it for subdomains only which has wildcard enabled.
####! Use it only after filter-resolving the results.
import sys,requests,threading,queue,os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
scan_type = str(sys.argv[1])
domain = str(sys.argv[2])
offset = int(sys.argv[3])

q = queue.Queue()
N_THREADS = 20
WILDCARD = True
threading_list = []

def CheckWildCard(subdomain):
    domains_wildcards = []
    response_lengths = [] 
    domains_wildcards.append('https://'+str(subdomain))
    domains_wildcards.append('http://'+str(subdomain))
    domains_wildcards.append('http://wildcardchecksggg'+str(subdomain))
    domains_wildcards.append('https://wildcardchecksggg'+str(subdomain))
    for each_url in domains_wildcards:
        try:
            req = len(requests.get(each_url,verify=False,timeout=5).content)
            response_lengths.append(req)
        except:
            response_lengths.append(0)
            pass
    reslen = list(set(response_lengths))
    max_res = max(reslen)
    reslen = [x for x in reslen if x != int(max_res)]
    if len(reslen) == 1 and reslen[0] == 0:
        print("VALID:"+str(subdomain))
        return
    else:
        for each_res in reslen:
            if (max_res - each_res <= int(offset)) == True:
                print("WILDCARD:"+str(subdomain))
                return
            else:
                print("VALID:"+str(subdomain))
                return

def ProcessQueue():
    while not q.empty():
        subdomain = q.get()
        CheckWildCard(subdomain)
        q.task_done()

if scan_type == 'list':
    with open(domain,'r') as f:
        for i in f.readlines():
            i = i.strip()
            if i.count('.') > 1:
                q.put(str(i))
            else:
                print("VALID:"+str(i))

    for i in range(N_THREADS):
        t = threading.Thread(target=ProcessQueue)
        threading_list.append(t)
        t.start() 

    for j in threading_list:
        j.join()
else:
    if domain.count('.') > 1:
        CheckWildCard(domain)
    else:
        print("VALID:"+str(domain))
