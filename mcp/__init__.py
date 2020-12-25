# Self check
from .internal_procedures.self_check import check_source

check_source()

# Create config_data
from .operate.config import load_config

config_data = load_config()

# Check update
from .internal_procedures.update import check_update

if config_data["auto_update"] or config_data["check_update"]:
    check_update(config_data["auto_update"])

# Delete not use/internal method
del check_source, config_data, load_config

from . import operate
from .operate.config import config

__all__ = ["check_update", "config", "operate"]
