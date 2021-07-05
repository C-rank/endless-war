from ew.static import cfg as ewcfg
from . import slimernaliacmds

cmd_map = {
	# Check your current festivity
    ewcfg.cmd_festivity: slimernaliacmds.festivity,
    # Wrap a gift -- ewitem maybe?
    ewcfg.cmd_wrap: slimernaliacmds.wrap,
    # Yo, Slimernalia
    ewcfg.cmd_yoslimernalia: slimernaliacmds.yoslimernalia,
}