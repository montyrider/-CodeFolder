from configparser import ConfigParser


def saveGameState(configFileName, actOrSceneToSave):
    """
    Function that will allow you to save the state of the game to a config file
    :return:
    """
    section = 'stateSaved'
    option = 'location'
    # need to save to the configuration file
    config = ConfigParser()
    config.read(configFileName)
    config.set(section, option, actOrSceneToSave)
    print(config.get(section,option))




def keepplaying():
    pick = input("Do you want to continue y or n: ")
    run = False
    if pick == "y":
        run = True
    return run
