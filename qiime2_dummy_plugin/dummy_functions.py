import qiime2
import biom
from q2_types.feature_table import FeatureTable, RelativeFrequency, BIOMV210DirFmt, PercentileNormalized


def dummy_function(input_artifact: FeatureTable[RelativeFrequency]) -> FeatureTable[PercentileNormalized] :
    print("dummy_function")
    # You can perform some processing on the input artifact and return a new artifact
    norm_biom = biom.Table(
        data=norm_df.values,
        observation_ids=norm_df.index,
        sample_ids=norm_df.columns)
    return norm_biom

