if  sys.version_info < (3,0):
    from scapy.all import *
else:
    from kamene.all import *
import random,socket,requests
def get_public_dns(timeout=10):
 try:
  return (requests.get('https://public-dns.info/nameservers.txt',timeout=timeout).text).split('\n')
 except:
  return []
def memcache_fact(u,timeout=3):
 req = IP(dst=u)/UDP(sport=random.randint(1025,65500),dport=11211)/Raw(load="\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n")
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,11211))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'memcache','ip':u,'sent':a,'received':b,'amplification_factor':c}
def dns_fact(u,timeout=3,q='google.com',t='ANY'):
 req = IP(dst=u)/UDP(sport=random.randint(1025,65500),dport=53)/DNS(rd=1, qd=DNSQR(qname=q,qtype=t))
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,53))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'dns','ip':u,'sent':a,'received':b,'amplification_factor':c}
def chargen_fact(u,timeout=3,q='0'):
 req = IP(dst=u)/UDP(sport=random.randint(1025,65500),dport=19)/q
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,19))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'chargen','ip':u,'sent':a,'received':b,'amplification_factor':c}
def ntp_fact(u,timeout=3):
 req = IP(dst=u)/UDP(sport=random.randint(1025,65500),dport=123)/Raw(load='\x17\x00\x02\x2a'+'\x00'*4)
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,123))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'ntp','ip':u,'sent':a,'received':b,'amplification_factor':c}
def ssdp_fact(u,timeout=3):
 req = IP(dst=u)/UDP(sport=random.randint(1025,65500),dport=1900)/Raw(load='M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: "ssdp:discover"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n')
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,1900))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'ssdp','ip':u,'sent':a,'received':b,'amplification_factor':c}
def snmp_fact(u,timeout=3):
 req=IP( dst=u)/UDP(sport=random.randint(1025,65500),dport=161)/Raw(load='\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa5\x19\x02\x04\x71\xb4\xb5\x68\x02\x01\x00\x02\x01\x7F\x30\x0b\x30\x09\x06\x05\x2b\x06\x01\x02\x01\x05\x00')
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,161))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'snmp','ip':u,'sent':a,'received':b,'amplification_factor':c}
def ping_fact(u,q='a',timeout=3):
 req=IP( dst=u)/UDP(sport=random.randint(1025,65500),dport=7)/Raw(load=q)
 s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
 s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
 s.sendto(bytes(req),(u,7))
 s.settimeout(timeout)
 d=''
 while True:
  try:
   o=''
   o+=s.recv(4096)
  except:
   pass
  if len(o)==0:
   break
  else:
   d+=o
 a=len(req)
 b=len(d)
 c=round(((len(d)*1.)/len(req)),3)
 return {'protocol':'echo','ip':u,'sent':a,'received':b,'amplification_factor':c}