"""Stands in for an SDK module (client_utils, file_utils...) that looks PluginsController up at import time."""
import java

_PluginsController = java.jclass("com.solegram.messenger.plugins.PluginsController")


def get_queue():
    return _PluginsController.pluginsQueue
