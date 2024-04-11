if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    data.dropna(inplace=True)
    data['title'] = data['title'].map(lambda x: x.strip() if isinstance(x, str) else x)
    data['article'] = data['article'].map(lambda x: x.strip() if isinstance(x, str) else x)
    data['len_title'] = [len(data) for data in data['title']]
    data['len_article'] = [len(data) for data in data['article']]
    data.drop(columns=['article', 'title'], inplace=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output.isnull().values.any() == False, 'There are rows with NaN'
