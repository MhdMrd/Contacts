import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.basename(BASE_DIR)))
CDIR = os.path.join(BASE_DIR, 'repertoire_app\static')

print "CDIR:"+CDIR

print "On est a :"+BASE_DIR
print "Le repertoire parent est:"+PARENT_DIR