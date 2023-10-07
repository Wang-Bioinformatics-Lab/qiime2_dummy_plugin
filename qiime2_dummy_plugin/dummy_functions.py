import qiime2
from q2_types.feature_table import FeatureTable, RelativeFrequency

def dummy_function(input_artifact: FeatureTable[RelativeFrequency]) -> FeatureTable[RelativeFrequency]:
    print("dummy_function")
    # Simply return the input artifact as-is
    return input_artifact

