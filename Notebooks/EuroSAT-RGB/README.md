---
license: mit
task_categories:
  - image-classification
task_ids:
  - multi-class-image-classification
language:
  - en
tags:
  - remote-sensing
  - satellite-imagery
  - land-use
  - land-cover
  - sentinel-2
  - earth-observation
  - eurosat
pretty_name: EuroSAT RGB
size_categories:
  - 10K<n<100K
source_datasets:
  - original
---

# EuroSAT RGB

## Dataset Description

EuroSAT is a dataset for land use and land cover (LULC) classification using Sentinel-2 satellite imagery. This version contains the RGB (visible spectrum) bands encoded as JPEG images at 64x64 pixel resolution.

The dataset covers 10 land use/land cover classes across 27,000 geo-referenced images from 34 European countries.

- **Source:** <https://zenodo.org/records/7711810>
- **DOI:** [10.5281/zenodo.7711810](https://doi.org/10.5281/zenodo.7711810)
- **License:** MIT
- **Paper:** [EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification](https://doi.org/10.1109/JSTARS.2019.2918242)

## Authors

Patrick Helber, Benjamin Bischke, Andreas Dengel, Damian Borth

## Dataset Structure

### Splits

| Split      | Examples |
|------------|----------|
| train      | 18,900   |
| validation | 5,400    |
| test       | 2,700    |

### Classes

| Label | Class Name            |
|-------|-----------------------|
| 0     | AnnualCrop            |
| 1     | Forest                |
| 2     | HerbaceousVegetation  |
| 3     | Highway               |
| 4     | Industrial            |
| 5     | Pasture               |
| 6     | PermanentCrop         |
| 7     | Residential           |
| 8     | River                 |
| 9     | SeaLake               |

### Features

- `image`: 64x64 RGB JPEG satellite image
- `label`: Integer class label (0–9)
- `filename`: Original filename with class directory prefix

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("giswqs/EuroSAT_RGB")

# Access training split
train = dataset["train"]
print(train[0])
```

## Citation

```bibtex
@article{helber2019eurosat,
  title={EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification},
  author={Helber, Patrick and Bischke, Benjamin and Dengel, Andreas and Borth, Damian},
  journal={IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing},
  volume={12},
  number={7},
  pages={2217--2226},
  year={2019},
  doi={10.1109/JSTARS.2019.2918242},
  publisher={IEEE}
}
```
