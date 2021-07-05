from ew.static import cfg as ewcfg
from . import dhcmds

cmd_map = {
	ewcfg.cmd_spook: dhcmds.spook
}