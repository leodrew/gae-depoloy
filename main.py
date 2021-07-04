import os, sys
exec(open("./env/bin/activate_this.py").read(), {'__file__': "/env/bin/activate_this.py"})
sys.path.append('./env/web')
sys.path.append('./env/lib/python3.8/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
from web.wsgi import application

app = application