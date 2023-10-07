import qiime2
from .dummy_functions import dummy_function
from q2_types.feature_table import FeatureTable, RelativeFrequency, BIOMV210DirFmt, PercentileNormalized

plugin = qiime2.plugin.Plugin(
    name='dummy-plugin',
    version='0.1.0',
    website='https://github.com/pluckySquid/qiime2_dummy_plugin.git',
    package='qiime2_dummy_plugin',
    description='A QIIME 2 plugin for dummy functions.',
    short_description='Plugin for dummy analysis.',
)

plugin.methods.register_function(
    function=dummy_function,
    inputs={'input_artifact': FeatureTable[RelativeFrequency]},
    parameters={},  # Add parameters if necessary
    outputs=[('perc_norm_table', FeatureTable[PercentileNormalized])],
    output_descriptions={
        'perc_norm_table': ('The percentile-normalized OTU table. '
            'If multiple batches were given, this table contains '
            'data which was percentile-normalized within each batch and '
            'then merged. Note that some OTUs may be filtered from certain '
            'batches if they are too infrequent within that batch. These '
            'will be NaN in the output OTU table.')},
    name='dummy-function',
    description='A description of your function.',
)