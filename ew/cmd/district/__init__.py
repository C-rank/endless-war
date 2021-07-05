from ew.static import cfg as ewcfg
from . import districtcmds

cmd_map = {

    # Check your current POI capture progress
    ewcfg.cmd_capture_progress: districtcmds.capture_progress,

    # Change your current POI capture progress
    # ewcfg.cmd_annex: cmds.annex,
    # ewcfg.cmd_annex_alt1: cmds.annex,

    # Change and use your graffiti signature
    ewcfg.cmd_changespray: districtcmds.change_spray,
    ewcfg.cmd_tag: districtcmds.tag,

}

apt_dm_cmd_map = {

    # something with capping
    ewcfg.cmd_changespray: districtcmds.change_spray,
    ewcfg.cmd_tag: districtcmds.tag,

}

# If we're using idle capping, spray becomes a tag alt
if ewcfg.capping_style == "idle":
    cmd_map[ewcfg.cmd_spray] = districtcmds.tag,
    cmd_map[ewcfg.cmd_spray_alt1] = districtcmds.tag

# Only enable these commands if the GvS event is active
if ewcfg.gvs_active:
    cmd_map[ewcfg.cmd_shamble] = districtcmds.shamble
    cmd_map[ewcfg.cmd_rejuvenate] = districtcmds.rejuvenate
