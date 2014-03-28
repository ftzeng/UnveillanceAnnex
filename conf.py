import os, yaml
from collections import namedtuple

HOST = os.getenv('UV_SERVER_HOST')
UUID = os.getenv('UV_UUID')

this_dir = os.path.abspath(os.path.join(__file__, os.pardir))
CONF_ROOT = os.path.join(this_dir, "conf")

with open(os.path.join(CONF_ROOT, "annex.config.yaml"), 'rb') as C:
	config = yaml.load(C.read())
	ANNEX_DIR = config['annex_dir']
	BASE_DIR = config['base_dir']
	MONITOR_ROOT = os.path.join(BASE_DIR, ".monitor")
	ELS_ROOT = os.path.join(BASE_DIR, config['els_root'])
	
with open(os.path.join(CONF_ROOT, "annex.settings.yaml"), 'rb') as C:
	config = yaml.load(C.read())
	API_PORT = config['api.port']
	NUM_PROCESSES = config['api.num_processes']