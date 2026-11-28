def run(ctx):
    # the plugin is the first to import an SDK module that takes PluginsController at import: the SDK's own look-up
    import sdk_client_utils
    sdk_client_utils.get_queue()
    return "sdk module loaded"
