import os
import json

from ..tools.path import run_here

__all__ = ["load_config", "config"]


@run_here
def load_config(paras=None):
    os.chdir("..")
    with open("config.json", encoding="UTF-8") as config_file:
        config_data = json.load(config_file)

    if paras is None:
        return config_data
    if type(paras) == list:
        values = []

        for para in paras:
            try:
                value = config_data[para]
                values.append(value)
            except ValueError:
                print(f'Invalid para: "{para}"')
                return

        return values
    if paras in config_data.keys():
        return config_data[paras]

    print(f'Invalid para: "{paras}"')


def config(**para):
    config_data = load_config()
    print(*config_data)
    # valid_para = dict(zip(*config_data))

    if len(para) == 0:
        return json.dumps(config_data, sort_key=True, indent="\t")
    if option_check(para, config_data, type_check=True):

        @run_here
        def update_config():
            # Generate changelog and update config_data
            for k, v in para.items():
                if config_data[k] != v:
                    changelog = changelog + f'\n\t"{k}": {config_data[k]} -> {v}'
                    config_data[k] = v

                # Save config_data to config.json
            os.chdir("..")
            with open("config.json", "w", encoding="UTF-8") as config_file:
                json.dump(config_data, config_file, indent="\t")

            return changelog
