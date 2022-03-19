from image import Image
import os

class AssetBank:
    """
    AssetBank holds assets in a dictionary to look up at any time
    """
    def __init__(self):
        """
        Creates a new AssetBank
        """
        self.__assets = {}

    def save_asset(self, name, obj):
        """
        Save an asset under the name
        Parameters:
            name (str) Name to store under
            obj (Any) Asset to store
        """
        self.__assets[name] = obj

    def get_asset(self, name):
        """
        Returns the asset under the name
        """
        return self.__assets[name]


ASSET_BANK = AssetBank()


def init_assets():
    for file in os.listdir("assets"):
        ASSET_BANK.save_asset(file, Image("assets/" + file))