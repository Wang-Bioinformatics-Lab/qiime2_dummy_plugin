# qiime2_dummy_plugin
This is a dummy plugin for qiime2


## to build:
```
pip install .
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

