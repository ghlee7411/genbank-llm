import os
import yaml
import json
from Bio import SeqIO
from tqdm import tqdm


def genbank_record_generator(genbank_file_path):
    with open(genbank_file_path, "r") as genbank_file:
        for record in tqdm(SeqIO.parse(genbank_file, "genbank"), desc="Saving genbank records to txt files"):
            yield record.format("genbank")