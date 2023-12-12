from typing import List
import random
import json

label2i = { 'Contradiction': 0, 'Entailment': 1 }

def groupDataByLabel(labels: List[int], texts: List[str], label2i: dict[str, int]) -> dict[int, List[str]]:
    data_by_label = {}
    for lab, text in zip(labels, texts):
        lab = label2i[lab]
        if lab not in data_by_label:
            data_by_label[lab] = []
        data_by_label[lab].append(text)
    return data_by_label

def split_dataset(labels, texts, label2i, proportion = .9):
    """
    Split the dataset randomly into training (proportion) and development (1-proportion) set
    Make sure the splits have the same label distribution
    """
    data_by_label = groupDataByLabel(labels, texts, label2i)

    random.shuffle(data_by_label[1])
    random.shuffle(data_by_label[0])

    split_1 = int(proportion * len(data_by_label[1]))
    split_0 = int(proportion * len(data_by_label[0]))

    return data_by_label[1][0:split_1] + data_by_label[0][0:split_0], [1] * split_1 + [0] * split_0, data_by_label[1][split_1:] + data_by_label[0][split_0:], [1] * (len(data_by_label[1]) - split_1) + [0] * (len(data_by_label[0]) - split_0)

def label_distribution(labels: List[int]):
    print("--- Entailment Count ---")
    print(sum(1 for l in labels if l == 1))
    print("\n--- Contradiction Count ---")
    print(sum(1 for l in labels if l == 0))

def read_dataset(train_path, validation_path, proportion = .9):
    with open(train_path) as json_file:
        train_data_raw = json.load(json_file)
    train_data_raw_keys = list(train_data_raw.keys())
    with open(validation_path) as json_file:
        validation_data_raw = json.load(json_file)
    validation_data_raw_keys = list(validation_data_raw.keys())

    train_sentences, train_labels, dev_sentences, dev_labels = split_dataset([train_data_raw[k]['Label'] for k in train_data_raw_keys], [train_data_raw[k]['Statement'] for k in train_data_raw_keys], label2i, proportion)
    validation_labels, validation_sentences = [label2i[validation_data_raw[k]['Label']] for k in validation_data_raw_keys], [validation_data_raw[k]['Statement'] for k in validation_data_raw_keys]

    return train_sentences, train_labels, dev_sentences, dev_labels, validation_sentences, validation_labels

def write_split_dataset(train_path, validation_path, output_path, proportion = .9):
    dataset = read_dataset(train_path, validation_path, proportion)
    with open(output_path, 'w') as json_file:
        json_file.write(json.dumps({ 'train': [dataset[0], dataset[1]], 'dev': [dataset[2], dataset[3]], 'validation': [dataset[4], dataset[5]] }))

def read_split_dataset(input_path):
    with open(input_path) as json_file:
        dataset = json.load(json_file)
        return dataset['train'][0], dataset['train'][1], dataset['dev'][0], dataset['dev'][1], dataset['validation'][0], dataset['validation'][1]
