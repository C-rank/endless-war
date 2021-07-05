from ew.utils import frontend as fe_utils

async def spook(cmd):
    # user_data = EwUser(member=cmd.message.author)
    await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, '\n' "***SPOOKED YA!***" + '\n' + "https://www.youtube.com/watch?v=T-dtcIXZo4s"))
