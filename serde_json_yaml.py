import argparse
import json

import yaml


def serde_json_to_yaml(json_file, create_output):
    # with open(json_file, "r") as f:
    #     json_data = json.load(f)
    # with open(json_file.replace(".json", ".yaml"), "w") as f:
    #     yaml.dump(json_data, f, default_flow_style=False)

    with open(json_file, "r") as f:
        data = f.read()
        yaml_data = yaml.dump(json.loads(data), sort_keys=False)
        # check if the output file is provided
        if create_output:
            # write the yaml data to the output file
            with open(json_file.replace(".json", ".yaml"), "w") as f:
                yaml.dump(yaml_data, f, default_flow_style=False)
        else:
            # print the yaml data to the console
            print(yaml_data)


def serde_yaml_to_json(yaml_file, create_output):
    # with open(yaml_file, "r") as f:
    #     yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    # with open(yaml_file.replace(".yaml", ".json"), "w") as f:
    #     json.dump(yaml_data, f)

    with open(yaml_file, "r") as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)

        if create_output:
            # write the yaml data to the output file
            with open(yaml_file.replace(".yaml", ".json"), "w") as f:
                json.dump(yaml_data, f)
        else:
            # print the yaml data to the console
            print(json.dumps(yaml_data, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Serde JSON file to YAML or vice versa"
    )
    parser.add_argument("file", type=str, help="File to be converted")
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        help="Type of conversion: json2yaml or yaml2json",
        required=True,
    )
    parser.add_argument("--output", action="store_true", help="Create an output file")
    args = parser.parse_args()
    file = args.file
    file_type = args.type
    output = args.output
    if file_type == "json2yaml":
        serde_json_to_yaml(file, output)
    elif file_type == "yaml2json":
        serde_yaml_to_json(file, output)
    else:
        print(
            "Invalid conversion type. Please choose either 'json2yaml' or 'yaml2json'."
        )
