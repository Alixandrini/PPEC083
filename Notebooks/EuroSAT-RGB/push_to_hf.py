"""Push EuroSAT_RGB dataset to Hugging Face Hub."""

import json
from pathlib import Path

import pandas as pd
from datasets import ClassLabel, Dataset, DatasetDict, Features, Image, Value
from huggingface_hub import HfApi

DATASET_DIR = Path("/path/to/EuroSAT_RGB")
HF_REPO_ID = "giswqs/EuroSAT_RGB"

# Load label map and build ordered class names
with open(DATASET_DIR / "label_map.json") as f:
    label_map = json.load(f)

class_names = [name for name, _ in sorted(label_map.items(), key=lambda x: x[1])]

features = Features(
    {
        "image": Image(),
        "label": ClassLabel(names=class_names),
        "filename": Value("string"),
    }
)


def load_split(csv_path: Path) -> Dataset:
    """Load a dataset split from a CSV file.

    Args:
        csv_path: Path to the CSV file containing split information.

    Returns:
        A Dataset with image, label, and filename columns.
    """
    df = pd.read_csv(csv_path, index_col=0)
    records = []
    for _, row in df.iterrows():
        records.append(
            {
                "image": str(DATASET_DIR / row["Filename"]),
                "label": int(row["Label"]),
                "filename": row["Filename"],
            }
        )
    return Dataset.from_list(records, features=features)


# Build DatasetDict
print("Loading splits...")
dataset_dict = DatasetDict(
    {
        "train": load_split(DATASET_DIR / "train.csv"),
        "validation": load_split(DATASET_DIR / "validation.csv"),
        "test": load_split(DATASET_DIR / "test.csv"),
    }
)

print(f"Train: {len(dataset_dict['train'])} examples")
print(f"Validation: {len(dataset_dict['validation'])} examples")
print(f"Test: {len(dataset_dict['test'])} examples")

# Push dataset to hub
print("Pushing dataset to Hugging Face Hub...")
dataset_dict.push_to_hub(HF_REPO_ID, private=False)

# Push README.md dataset card
print("Pushing dataset card...")
api = HfApi()
api.upload_file(
    path_or_fileobj=str(DATASET_DIR / "README.md"),
    path_in_repo="README.md",
    repo_id=HF_REPO_ID,
    repo_type="dataset",
)

print(f"Done! Dataset available at https://huggingface.co/datasets/{HF_REPO_ID}")
