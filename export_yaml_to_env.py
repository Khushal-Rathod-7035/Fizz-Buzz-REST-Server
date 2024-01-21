"""Convert environments/{development or production}-env.yml file to .env file.
 """
import sys
import yaml


def export_to_env(file_yaml_loc, file_env_loc):
    """Convert environments/{development or production}-env.yml file to .env file.

        Args:
            file_yaml_loc (str): Path to the YAML file.
            file_env_loc (str): Path to the .env file.
        """
    try:
        with open(file_yaml_loc, 'r', encoding='utf-8') as file_yaml:
            data = yaml.safe_load(file_yaml)

        with open(file_env_loc, 'w', encoding='utf-8') as file_env:
            for key, value in data.items():
                file_env.write(f'{key}={value}\n')

        print(f'Successfully exported data from {yaml_file} to {env_file}')
    except Exception as error:
        print(f'Error: {error}')


if __name__ == "__main__":
    yaml_file = sys.argv[1]
    env_file = sys.argv[2]
    export_to_env(yaml_file, env_file)
