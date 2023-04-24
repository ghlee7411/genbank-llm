import os
import yaml
import json
from Bio import SeqIO
from tqdm import tqdm


def read_config_openai_api_key(config_file='config.yml'):
    """
    Read the config.yaml file and save the openai api key into an environment variable
    :param config_file: the config.yaml file
    :return: None
    """
    with open(config_file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            os.environ['API_KEY'] = config['openai-api-key']
        except yaml.YAMLError as exc:
            print(exc)


def save_genbank_records_to_txt_files(genbank_file_path, output_dir, max_records=1000):
    with open(genbank_file_path, "r") as genbank_file:
        for record in tqdm(SeqIO.parse(genbank_file, "genbank"), desc="Saving genbank records to txt files"):
            output_file_path = f"{output_dir}/{record.id}.gb"
            
            # if the output file already exists, skip it
            if os.path.exists(output_file_path):
                continue
            
            # if the directory is not created, create it
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            with open(output_file_path, "w") as output_file:
                output_file.write(record.format("genbank"))
            
            if max_records > 0 and len(os.listdir(output_dir)) >= max_records:
                break


def main(genbank_file, output_dir):
    read_config_openai_api_key()
    save_genbank_records_to_txt_files(genbank_file, output_dir)


if __name__ == '__main__':
    # get the input genbank file path from the command line using argparse
    # https://docs.python.org/3/library/argparse.html
    import argparse
    parser = argparse.ArgumentParser(description='Analyze a document using the langchain model')
    parser.add_argument('genbank_file', type=str, help='The path to the genbank file')
    parser.add_argument('output_dir', type=str, help='The path to the output directory')
    args = parser.parse_args()
    main(args.genbank_file, args.output_dir)
