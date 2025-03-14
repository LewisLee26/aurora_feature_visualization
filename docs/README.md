# Aurora Feature Visualisation

**Description/Summary**

## Set up

### Environments
```bash
conda env create -f requirements.yml
```

### Checkpoints
[Hugging Face Aurora](https://huggingface.co/microsoft/aurora)

```bash
curl https://huggingface.co/microsoft/aurora/resolve/main/aurora-0.25-small-pretrained.ckpt -o aurora-0.25-small-pretrained.ckpt
```

## Run Scripts
Run from root of repo

```bash
conda activate aurora_fv
python scripts/download_data.py
```

```bash
conda activate aurora_fv
python scripts/aurora_inference.py
```
