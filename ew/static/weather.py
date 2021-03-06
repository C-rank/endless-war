from . import cfg as ewcfg

from ..model.weather import EwWeather

# All weather effects in the game.
weather_list = [
    EwWeather(
        name=ewcfg.weather_sunny,
        sunrise="The smog is beginning to clear in the sickly morning sunlight.",
        day="The sun is blazing on the cracked streets, making the air shimmer.",
        sunset="The sky is darkening, the low clouds an iridescent orange.",
        night="The moon looms yellow as factories belch smoke all through the night."
    ),
    EwWeather(
        name=ewcfg.weather_rainy,
        sunrise="Rain gently beats against the pavement as the sky starts to lighten.",
        day="Rain pours down, collecting in oily rivers that run down sewer drains.",
        sunset="Distant thunder rumbles as it rains, the sky now growing dark.",
        night="Silverish clouds hide the moon, and the night is black in the heavy rain."
    ),
    EwWeather(
        name=ewcfg.weather_windy,
        sunrise="Wind whips through the city streets as the sun crests over the horizon.",
        day="Paper and debris are whipped through the city streets by the winds, buffetting pedestrians.",
        sunset="The few trees in the city bend and strain in the wind as the sun slowly sets.",
        night="The dark streets howl, battering apartment windows with vicious night winds."
    ),
    EwWeather(
        name=ewcfg.weather_lightning,
        sunrise="An ill-omened morning dawns as lighting streaks across the sky in the sunrise.",
        day="Flashes of bright lightning and peals of thunder periodically startle the citizens out of their usual stupor.",
        sunset="Bluish white arcs of electricity tear through the dusky, deep-red sky.",
        night="The dark night periodically lights with bright whitish-green bolts that flash off the metal and glass of skyscrapers."
    ),
    EwWeather(
        name=ewcfg.weather_cloudy,
        sunrise="The dim morning light spreads timidly across the thickly clouded sky.",
        day="The air hangs thick, and the pavement is damp with mist from the clouds overhead.",
        sunset="The dusky light blares angry red on a sky choked with clouds and smog.",
        night="Everything is dark and still but the roiling clouds, reflecting the city's eerie light."
    ),
    EwWeather(
        name=ewcfg.weather_snow,
        sunrise="The morning sun glints off the thin layer of powdery snow that blankets the city.",
        day="Flakes of snow clump together and whip through the bitter cold air in the winter wind.",
        sunset="The chilly air grows colder as the sky darkens and snow piles higher in the streets.",
        night="Icy winds whip through the city, white snowflakes glittering in the black of night."
    ),
    EwWeather(
        name=ewcfg.weather_foggy,
        sunrise="Fog hangs thick in the air, stubbornly refusing to dissipate as the sun clears the horizon.",
        day="You can barely see to the next block in the sickly greenish NLACakaNM smog.",
        sunset="Visibility only grows worse in the fog as the sun sets and the daylight fades.",
        night="Everything is obscured by the darkness of night and the thick city smog."
    ),
    # EwWeather(
    #  	name = ewcfg.weather_bicarbonaterain,
    #  	sunrise = "Accursed bicarbonate soda and sugar rain blocks out the morning sun.",
    #  	day = "The bicarbonate rain won't let up. That blue weasel is going to pay for this.",
    #  	sunset = "The deadly rain keeps beating down mercilessly. You have a feeling it's going to be a long night.",
    #  	night = "Clouds of doom obscure the moon as they dispense liquid death from above."
    # ),
]

# A map of name to EwWeather objects.
weather_map = {}
for weather in weather_list:
    weather_map[weather.name] = weather
