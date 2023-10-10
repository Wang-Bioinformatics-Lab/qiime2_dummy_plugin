import qiime2
import biom
import qiime2.plugin
from q2_types.feature_table import FeatureTable, RelativeFrequency


def dummy_function(input_artifact: biom.Table) -> biom.Table:
    # this is a dummy plugin, just do nothing but to have a return to make sure it is working
    return input_artifact

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
    outputs=[('output_artifact', FeatureTable[RelativeFrequency])],
    output_descriptions={
        'output_artifact': 'Description of the output artifact.'
    },
    name='dummy-function',
    description='A description of your function.',
)