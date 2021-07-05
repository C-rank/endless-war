from ew.static import cfg as ewcfg
from . import gvscmds

cmd_map = {
	ewcfg.cmd_gvs_printgrid: gvscmds.gvs_print_grid,
    ewcfg.cmd_gvs_printgrid_alt1: gvscmds.gvs_print_grid,
    ewcfg.cmd_gvs_printlane: gvscmds.gvs_print_lane,
    ewcfg.cmd_gvs_incubategaiaslimeoid: gvscmds.gvs_incubate_gaiaslimeoid,
    ewcfg.cmd_gvs_fabricatetombstone: gvscmds.gvs_fabricate_tombstone,
    ewcfg.cmd_gvs_joinoperation: gvscmds.gvs_join_operation,
    ewcfg.cmd_gvs_leaveoperation: gvscmds.gvs_leave_operation,
    ewcfg.cmd_gvs_checkoperation: gvscmds.gvs_check_operations,
    ewcfg.cmd_gvs_plantgaiaslimeoid: gvscmds.gvs_plant_gaiaslimeoid,
    ewcfg.cmd_gvs_searchforbrainz: gvscmds.gvs_searchforbrainz,
    ewcfg.cmd_gvs_grabbrainz: gvscmds.gvs_grabbrainz,
    ewcfg.cmd_gvs_dive: gvscmds.gvs_dive,
    ewcfg.cmd_gvs_resurface: gvscmds.gvs_resurface,
    ewcfg.cmd_gvs_sellgaiaslimeoid: gvscmds.gvs_sell_gaiaslimeoid,
    ewcfg.cmd_gvs_sellgaiaslimeoid_alt: gvscmds.gvs_sell_gaiaslimeoid,
    ewcfg.cmd_gvs_dig: gvscmds.dig,
    ewcfg.cmd_gvs_progress: gvscmds.gvs_progress,
    ewcfg.cmd_gvs_gaiaslime: gvscmds.gvs_gaiaslime,
    ewcfg.cmd_gvs_gaiaslime_alt1: gvscmds.gvs_gaiaslime,
    ewcfg.cmd_gvs_brainz: gvscmds.gvs_brainz,
	ewcfg.cmd_shamble: gvscmds.shamble,
    ewcfg.cmd_rejuvenate: gvscmds.rejuvenate
}

dm_cmd_map = {
	ewcfg.cmd_gvs_grabbrainz: gvscmds.gvs_grabbrainz,
}
    
