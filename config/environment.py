ENVIRONMENT = "local"
# ENVIRONMENT = "testing"
# ENVIRONMENT = "production"

SETTINGS_MODULE = "config.settings.local"

if ENVIRONMENT == "local":
    SETTINGS_MODULE = "config.settings.local"
if ENVIRONMENT == "testing":
    SETTINGS_MODULE = "config.settings.testing"
if ENVIRONMENT == "production":
    SETTINGS_MODULE = "config.settings.production"
