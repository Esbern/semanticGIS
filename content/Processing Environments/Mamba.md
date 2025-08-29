---
title: Mamba
draft: false
tags:
---
 
### Installing Mamba

```python
conda install -n base -c conda-forge mamba
```

### Adding channels

```python
conda config --add channels conda-forge
```

### Updating Mamba

```python
mamba update -n base mamba
```

### Finding a Package

```python
mamba repoquery search PACKAGE
```

### Searching for dependencies

```python
mamba repoquery depends -a PACKAGE
```

### Creating an environment

```python
mamba create -n ENV_NAME PACKAGE
mamba env create -f env.yml
```

### Adding/Updating software

```python
mamba install -n ENV_NAME PACKAGE
mamba update -n ENV_NAME --all
```

### Removing a package

```python
mamba remove -n ENV_NAME PACKAGE
```

### Undoing changes to an environment

```python
mamba list -n ENV_NAME --revisions
mamba install -n ENV_NAME --revision 1
```

### Show environment

```python
conda env export --no-builds
```

### Clone an existing environment

```python
conda create --name CLONE_ENV_NAME --clone ENV_NAME
```

### Removing an environment

```python
mamba env remove -n ENV_NAME
conda remove --name ENV_NAME --all
```

### Exporting an environment

```python
mamba env export -n ENV_NAME > ENV_NAME.yaml
conda list -e > ENV_NAME.txt
```

- **Windows**:

```python
conda env export -n ENV_NAME | findstr -v "prefix" > ENV_NAME.yaml
```

- **Linux**:

```python
conda env export -n ENV_NAME --no-builds | grep -v "prefix" > ENV_NAME.yaml
```

### Importing an environment

```python
mamba env create --file ENV_NAME.yaml
conda env create --file ENV_NAME.yaml
conda create -n ENV_NAME --file ENV_NAME.txt
```

### Deactivate the Environment

```python
conda deactivate
```

### Viewing a list of your environments

```python
conda info --envs
conda env list
```