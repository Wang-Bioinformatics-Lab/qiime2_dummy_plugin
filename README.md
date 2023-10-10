# qiime2_dummy_plugin
This is a dummy plugin for qiime2

## Install qiime2
Check if qiime2 update their install document. The default installation is using conda. 
Currently, the conda install have a problem, so we need to remove a line of the qiime2-2023.7-py38-linux-conda.yml.

### Install conda
You may reference here for how to install miniconda. \
https://github.com/Wang-Bioinformatics-Lab/Lab_Internal_Documentation/blob/ea43254cd7c732acf867549198545851600fa97b/docs/env_setup.md#setting-up-miniconda-deprecated

### Prepare the env
After installing Miniconda and opening a new terminal, make sure you’re running the latest version of conda:
```
conda update conda
```
Installing wget
```
conda install wget
```

### Install qiime2 with conda
```
wget https://data.qiime2.org/distro/core/qiime2-2023.7-py38-linux-conda.yml
conda env create -n qiime2-2023.7 --file qiime2-2023.7-py38-linux-conda.yml
```

If they have not update the yml, please remove the line "bioconductor-genomeinfodb" from qiime2-2023.7-py38-linux-conda.yml after wget, then try:
```
conda env create -n qiime2-2023.7 --file qiime2-2023.7-py38-linux-conda.yml
```
### Activate the environment
```
conda activate qiime2-2023.7
```

### Test your installation
You can test your installation by activating your QIIME 2 environment and running:
```
qiime --help
```
If no errors are reported when running this command, the installation was successful!


## to build:
```
pip install -e .
```

This should give you something like:
```
(qiime2-2023.7) user@yunshu:~/qiime2_dummy_plugin$ pip install .
Processing /home/user/qiime2_dummy_plugin
  Preparing metadata (setup.py) ... done
Requirement already satisfied: qiime2 in /home/user/miniconda3/envs/qiime2-2023.7/lib/python3.8/site-packages (from qiime2-dummy-plugin==0.1.0) (2023.7.0)
Building wheels for collected packages: qiime2-dummy-plugin
  Building wheel for qiime2-dummy-plugin (setup.py) ... done
  Created wheel for qiime2-dummy-plugin: filename=qiime2_dummy_plugin-0.1.0-py3-none-any.whl size=3017 sha256=28e3035c2606ae0d52ba1aa5e8cc8afbe76b06ccfc37b94856eddc097ea2c1ca
  Stored in directory: /tmp/pip-ephem-wheel-cache-9x5n7op6/wheels/92/fb/1f/fe409ace0bfc939ad31fac7fb7b56cd8e6b3573df856cf0478
Successfully built qiime2-dummy-plugin
Installing collected packages: qiime2-dummy-plugin
  Attempting uninstall: qiime2-dummy-plugin
    Found existing installation: qiime2-dummy-plugin 0.1.0
    Uninstalling qiime2-dummy-plugin-0.1.0:
      Successfully uninstalled qiime2-dummy-plugin-0.1.0
Successfully installed qiime2-dummy-plugin-0.1.0
```

##
To Run:
```
qiime dummy-plugin
```

The result should be something like this:
```

  Description: A QIIME 2 plugin for dummy functions.

  Plugin website: https://github.com/pluckySquid/qiime2_dummy_plugin.git

  Getting user support: Please post to the QIIME 2 forum for help with this
  plugin: https://forum.qiime2.org

Options:
  --version            Show the version and exit.
  --example-data PATH  Write example data and exit.
  --citations          Show citations and exit.
  --help               Show this message and exit.

Commands:
  dummy-function  dummy-function
  ```


## To test it
```
python setup.py install
```

After install, use this command:

```
qiime dummy-plugin dummy-function --i-input-artifact data/test_otu_table.transpose.qza --o-output-artifact data/output.qza
```

If the output is :
```
Saved FeatureTable[RelativeFrequency] to: data/output.qza
```

It proves the build is correct. 
