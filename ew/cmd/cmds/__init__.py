from ew.static import cfg as ewcfg
from . import cmdcmds

cmd_map = {

    # Show the current slime score of a player.
    ewcfg.cmd_score: cmdcmds.score,
    ewcfg.cmd_score_alt1: cmdcmds.score,
    ewcfg.cmd_score_alt2: cmdcmds.score,
    ewcfg.cmd_score_alt3: cmdcmds.score,

    # Show a player's combat data.
    ewcfg.cmd_data: cmdcmds.data,

    # Show a player's mutations.
    ewcfg.cmd_mutations: cmdcmds.mutations,
    ewcfg.cmd_mutations_alt_1: cmdcmds.mutations,

    # Check how hungry you are.
    ewcfg.cmd_hunger: cmdcmds.hunger,

    # check what time it is, and the weather
    ewcfg.cmd_time: cmdcmds.weather,
    ewcfg.cmd_clock: cmdcmds.weather,
    ewcfg.cmd_weather: cmdcmds.weather,

    # Rowdys thrash and Killers dab.
    ewcfg.cmd_thrash: cmdcmds.thrash,
    ewcfg.cmd_dab: cmdcmds.dab,

    # Ghosts can BOO
    ewcfg.cmd_boo: cmdcmds.boo,

    # Juvies can dance
    ewcfg.cmd_dance: cmdcmds.dance,
    ewcfg.cmd_dance_alt: cmdcmds.dance,

    # Terezi Gang can flip coins
    ewcfg.cmd_coinflip: cmdcmds.coinflip,

    # Bass weilders can jam out
    ewcfg.cmd_jam: cmdcmds.jam,

    # Show the total of positive slime in the world.
    ewcfg.cmd_endlesswar: cmdcmds.endlesswar,

    # Slimefest
    ewcfg.cmd_slimefest: cmdcmds.slimefest,

    # Show the number of swears in the global swear jar.
    # ewcfg.cmd_swear_jar: cmds.swearjar,

    # throw an item off the cliff
    # TODO -- Find out how to put this in item cmds without circular imports
    ewcfg.cmd_toss: cmdcmds.toss_off_cliff,

    # throw yourself off the cliff
    ewcfg.cmd_jump: cmdcmds.jump,
    ewcfg.cmd_jump_alt1: cmdcmds.jump,

    # throw someone else off the cliff -- could be in wep
    ewcfg.cmd_push: cmdcmds.push,
    ewcfg.cmd_push_alt_1: cmdcmds.push,
    ewcfg.cmd_push_alt_2: cmdcmds.push,

    # drink from the fountain
    ewcfg.cmd_purify: cmdcmds.purify,

    # look at the flag
    ewcfg.cmd_checkflag: cmdcmds.check_flag,

    # TODO - adapt these for every challenge/confrimation
    # Used in russianroulette and slimeoidbattle.
    ewcfg.cmd_accept: cmdcmds.accept,
    ewcfg.cmd_refuse: cmdcmds.refuse,

    # More confirmation cmds, but for ads
    ewcfg.cmd_confirm: cmdcmds.confirm,
    ewcfg.cmd_cancel: cmdcmds.cancel,

    # link to the world maps
    ewcfg.cmd_map: cmdcmds.map,
    ewcfg.cmd_transportmap: cmdcmds.transportmap,

    # Check your fashion ratings
    ewcfg.cmd_fashion: cmdcmds.fashion,
    ewcfg.cmd_fashion_alt1: cmdcmds.fashion,

    # Admin/debug commands
    ewcfg.cmd_setslime: cmdcmds.set_slime,
    ewcfg.cmd_checkstats: cmdcmds.check_stats,
    ewcfg.cmd_makebp: cmdcmds.make_bp,
    ewcfg.cmd_ping_me: cmdcmds.ping_me,
    ewcfg.cmd_addstatuseffect: cmdcmds.assign_status_effect,
    ewcfg.cmd_promote: cmdcmds.promote,
    ewcfg.cmd_checkbot: cmdcmds.check_bot,

    # force print the leaderboard
    ewcfg.cmd_post_leaderboard: cmdcmds.post_leaderboard,

    # Ban/pardon from gameplay
    ewcfg.cmd_arrest: cmdcmds.arrest,
    ewcfg.cmd_release: cmdcmds.release,
    ewcfg.cmd_release_alt1: cmdcmds.release,
    ewcfg.cmd_manual_unban: cmdcmds.unban_manual,

    # recycle your trash at the slimecorp recycling plant
    ewcfg.cmd_recycle: cmdcmds.recycle,
    ewcfg.cmd_recycle_alt1: cmdcmds.recycle,

    # Show guide pages or available commands
    ewcfg.cmd_help: cmdcmds.help,
    ewcfg.cmd_help_alt3: cmdcmds.help,
    ewcfg.cmd_commands: cmdcmds.commands,
    ewcfg.cmd_commands_alt1: cmdcmds.commands,

    # Pure flavor response
    ewcfg.cmd_howl: cmdcmds.cmd_howl,
    ewcfg.cmd_howl_alt1: cmdcmds.cmd_howl,
    ewcfg.cmd_moan: cmdcmds.cmd_moan,
    ewcfg.cmd_harvest: cmdcmds.harvest,
    ewcfg.cmd_salute: cmdcmds.salute,
    ewcfg.cmd_unsalute: cmdcmds.unsalute,
    ewcfg.cmd_hurl: cmdcmds.hurl,

    # Link to various external things
    ewcfg.cmd_news: cmdcmds.patchnotes,
    ewcfg.cmd_patchnotes: cmdcmds.patchnotes,
    ewcfg.cmd_wiki: cmdcmds.wiki,
    ewcfg.cmd_booru: cmdcmds.booru,
    ewcfg.cmd_bandcamp: cmdcmds.bandcamp,
    ewcfg.cmd_tutorial: cmdcmds.tutorial,
    ewcfg.cmd_leaderboard: cmdcmds.leaderboard,
    ewcfg.cmd_leaderboard_alt1: cmdcmds.leaderboard,

    # LOL
    ewcfg.cmd_lol: cmdcmds.lol,

    # Shuts down the bot with sys.exit()
    # or kills non admins
    ewcfg.cmd_shutdownbot: cmdcmds.shut_down_bot,

    ewcfg.cmd_set_debug_option: cmdcmds.set_debug_option,

    # for the filth
    ewcfg.cmd_paycheck: cmdcmds.paycheck,
    ewcfg.cmd_payday: cmdcmds.payday,

    # Praying at the base of ENDLESS WAR.
    ewcfg.cmd_pray: cmdcmds.pray,

    # Slimernalia -- please see bottom of file for commands

    # Swilldermuk -- please see bottom of file for other commands
    ewcfg.cmd_prank: cmdcmds.prank,

    # Gankers Vs. Shamblers -- please see bottom of file for other commands
    ewcfg.cmd_gvs_almanac: cmdcmds.almanac,
    

    # Check your weapon masteries
    ewcfg.cmd_mastery: cmdcmds.check_mastery,
    ewcfg.cmd_getattire: cmdcmds.get_attire,

    # SlimeCorp security officers can post propaganda
    # ewcfg.cmd_propaganda: ewcmd.propaganda,

    # Show the player's slime coin.
    ewcfg.cmd_slimecoin: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt1: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt2: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt3: cmdcmds.slimecoin,

    # show player's current shares in a company
    ewcfg.cmd_shares: cmdcmds.shares,
    ewcfg.cmd_shares_alt1: cmdcmds.shares,

}

dm_cmd_map = {

    # !help
    ewcfg.cmd_help: cmdcmds.help,
    ewcfg.cmd_help_alt3: cmdcmds.help,

    # !commands
    ewcfg.cmd_commands_alt1: cmdcmds.commands,
    ewcfg.cmd_commands: cmdcmds.commands,
    
}

apt_dm_cmd_map = {

    # !howl
    ewcfg.cmd_howl: cmdcmds.cmd_howl,
    ewcfg.cmd_howl_alt1: cmdcmds.cmd_howl,

    # !moan
    ewcfg.cmd_moan: cmdcmds.cmd_moan,

    # Show a player's combat data.
    ewcfg.cmd_data: cmdcmds.data,

    # Check how hungry you are.
    ewcfg.cmd_hunger: cmdcmds.hunger,

    # Show the current slime score of a player.
    ewcfg.cmd_score: cmdcmds.score,
    ewcfg.cmd_score_alt1: cmdcmds.score,
    ewcfg.cmd_score_alt2: cmdcmds.score,
    ewcfg.cmd_score_alt3: cmdcmds.score,

    # !booru
    ewcfg.cmd_booru: cmdcmds.booru,

    # !wiki
    ewcfg.cmd_wiki: cmdcmds.wiki,

    # !unsalute
    ewcfg.cmd_unsalute: cmdcmds.unsalute,

    # !salute
    ewcfg.cmd_salute: cmdcmds.salute,

    # vomit
    ewcfg.cmd_hurl: cmdcmds.hurl,

    # link to the world map
    ewcfg.cmd_map: cmdcmds.map,

    # check what time it is, and the weather
    ewcfg.cmd_time: cmdcmds.weather,
    ewcfg.cmd_clock: cmdcmds.weather,
    ewcfg.cmd_weather: cmdcmds.weather,

    # Check patchnotes
    ewcfg.cmd_news: cmdcmds.patchnotes,
    ewcfg.cmd_patchnotes: cmdcmds.patchnotes,

    # gives +10Gigaslime
    ewcfg.cmd_harvest: cmdcmds.harvest,

    # show what commands are currently available
    ewcfg.cmd_commands_alt1: cmdcmds.commands,
    ewcfg.cmd_commands: cmdcmds.commands,

    # Show the player's slime coin.
    ewcfg.cmd_slimecoin: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt1: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt2: cmdcmds.slimecoin,
    ewcfg.cmd_slimecoin_alt3: cmdcmds.slimecoin,

}

dh_cmd_map = {
    ewcfg.cmd_spook: cmdcmds.spook
}

slimernalia_cmd_map = {
    # Check your current festivity
    ewcfg.cmd_festivity: cmdcmds.festivity,
    # Wrap a gift -- ewitem maybe?
    ewcfg.cmd_wrap: cmdcmds.wrap,
    # Yo, Slimernalia
    ewcfg.cmd_yoslimernalia: cmdcmds.yoslimernalia,
}

swilldermuk_cmd_map = {
    ewcfg.cmd_gambit: cmdcmds.gambit,
    ewcfg.cmd_credence: cmdcmds.credence, #debug
    ewcfg.cmd_get_credence: cmdcmds.get_credence, #debug
    ewcfg.cmd_reset_prank_stats: cmdcmds.reset_prank_stats, #debug
    ewcfg.cmd_set_gambit: cmdcmds.set_gambit, #debug
    ewcfg.cmd_pointandlaugh: cmdcmds.point_and_laugh,
}

gvs_command_map = {
    ewcfg.cmd_gvs_printgrid: cmdcmds.gvs_print_grid,
    ewcfg.cmd_gvs_printgrid_alt1: cmdcmds.gvs_print_grid,
    ewcfg.cmd_gvs_printlane: cmdcmds.gvs_print_lane,
    ewcfg.cmd_gvs_incubategaiaslimeoid: cmdcmds.gvs_incubate_gaiaslimeoid,
    ewcfg.cmd_gvs_fabricatetombstone: cmdcmds.gvs_fabricate_tombstone,
    ewcfg.cmd_gvs_joinoperation: cmdcmds.gvs_join_operation,
    ewcfg.cmd_gvs_leaveoperation: cmdcmds.gvs_leave_operation,
    ewcfg.cmd_gvs_checkoperation: cmdcmds.gvs_check_operations,
    ewcfg.cmd_gvs_plantgaiaslimeoid: cmdcmds.gvs_plant_gaiaslimeoid,
    ewcfg.cmd_gvs_searchforbrainz: cmdcmds.gvs_searchforbrainz,
    ewcfg.cmd_gvs_grabbrainz: cmdcmds.gvs_grabbrainz,
    ewcfg.cmd_gvs_dive: cmdcmds.gvs_dive,
    ewcfg.cmd_gvs_resurface: cmdcmds.gvs_resurface,
    ewcfg.cmd_gvs_sellgaiaslimeoid: cmdcmds.gvs_sell_gaiaslimeoid,
    ewcfg.cmd_gvs_sellgaiaslimeoid_alt: cmdcmds.gvs_sell_gaiaslimeoid,
    ewcfg.cmd_gvs_dig: cmdcmds.dig,
    ewcfg.cmd_gvs_progress: cmdcmds.gvs_progress,
    ewcfg.cmd_gvs_gaiaslime: cmdcmds.gvs_gaiaslime,
    ewcfg.cmd_gvs_gaiaslime_alt1: cmdcmds.gvs_gaiaslime,
    ewcfg.cmd_gvs_brainz: cmdcmds.gvs_brainz,
}

gvs_dm_command_map = {
    ewcfg.cmd_gvs_grabbrainz: cmdcmds.gvs_grabbrainz,
}

if ewcfg.dh_active:
    cmd_map.extend(dh_cmd_map)

if ewcfg.slimernalia_active:
    cmd_map.extend(slimernalia_cmd_map)

if ewcfg.swilldermuk_active:
    cmd_map.extend(swilldermuk_cmd_map)

if ewcfg.gvs_active:
    cmd_map.extend(gvs_command_map)
    dm_cmd_map.extend(gvs_dm_command_map)
