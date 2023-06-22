
import random
import pandas as pd
import numpy as np
import dill

def select_merge_on(df):
    # Select either "on" or both "left_on" and "right_on", but not a combination
    if random.choice([True, False]):
        return random.choice([None] + list(df.columns)), None, None
    else:
        return None, random.choice([None] + list(df.columns)), random.choice([None] + list(df.columns))

def select_merge_index(_):
    # Select either "left_index" or both "left_index" and "right_index", but not both
    left_index = random.choice([False, True])
    right_index = random.choice([False, True]) if not left_index else False
    return left_index, right_index

def random_correlation_method(_):
    # Randomly select a method
    return random.choice(['pearson', 'kendall', 'spearman'])

def random_min_periods(_):
    # Randomly select a minimum number of periods (1 to 5)
    return random.randint(1, 5)

def random_round_decimals(df):
    # Randomly select an integer, dict, or Series for decimals
    choice = random.choice(['int', 'dict', 'series'])
    
    if choice == 'int':
        return random.randint(0, 5)
    
    if choice == 'dict':
        return {col: random.randint(0, 5) for col in df.columns}
    
    if choice == 'series':
        return pd.Series({col: random.randint(0, 5) for col in df.columns})

def random_min_periods_cov(_):
    # Randomly select a minimum number of periods (1 to 5) or None
    return random.choice([None, 1, 2, 3, 4, 5])

def random_ddof(_):
    # Randomly select delta degrees of freedom (0 or 1)
    return random.choice([0, 1])

def random_drop(_):
    # Randomly select whether to drop missing indices (True or False)
    return random.choice([True, False])

def random_correlation_method(_):
    # Randomly select a correlation method ('pearson', 'kendall', 'spearman') or a callable
    return random.choice(['pearson', 'kendall', 'spearman'])

def random_function(x):
    # Example: sum the elements of the series
    return x * x

class DataFrameMethodArgs:

    DEFAULT_METHOD_CONFIGS = {
        'sort_values': {
            'by': lambda df: random.choice(list(df.columns)),
            'axis': lambda _: random.choice([0]),
            'ascending': lambda _: random.choice([True, False]),
            'inplace': lambda _: random.choice([False]),
            'kind': lambda _: random.choice(['quicksort', 'mergesort', 'heapsort', 'stable']),
            'na_position': lambda _: random.choice(['first', 'last']),
            'ignore_index': lambda _: random.choice([True, False])
        },
        'merge': {
            'right': lambda df: random.choice([df for _ in range(10)]),
            'how': lambda _: random.choice(['left', 'right', 'outer', 'inner', 'cross']),
            'sort': lambda _: random.choice([False, True]),
            'suffixes': lambda _: ('_x', '_y'),
            'copy': lambda _: random.choice([False, True]),
            'indicator': lambda _: random.choice([False, True, '_merge']),
        },
        'round': {
            'decimals': random_round_decimals
        },
        'corr': {
            'method': random_correlation_method,
            'min_periods': random_min_periods,
            'numeric_only': lambda _: random.choice([True, False]),
        },
        'cov': {
            'min_periods': random_min_periods_cov,
            'ddof': random_ddof,
            'numeric_only': lambda _: random.choice([True, False]),
        },
        'corrwith': {
            'other': lambda df: random.choice([df for _ in range(10)]),
            'axis': lambda _: random.choice([0]),
            'drop': random_drop,
            'method': random_correlation_method,
            'numeric_only': lambda _: random.choice([True, False]),
        },
        'count': {
            'axis': lambda _: random.choice([0]),
            'numeric_only': lambda _: random.choice([True, False]),
        },
        'nunique': {
            'axis': lambda _: random.choice([0, 1, 'index', 'columns']),
            'dropna': lambda _: random.choice([True, False]),
        },
        'mode': {
            'axis': lambda _: random.choice([0, 1, 'index', 'columns']),
            'numeric_only': lambda _: random.choice([True, False]),
            'dropna': lambda _: random.choice([True, False]),
        },
        'quantile': {
            'q': lambda _: random.choice([random.uniform(0, 1), [random.uniform(0, 1) for _ in range(random.randint(1, 3))]]),
            'axis': lambda _: random.choice([0, 1, 'index', 'columns']),
            'numeric_only': lambda _: random.choice([True, False]),
            'interpolation': lambda _: random.choice(['lower', 'higher', 'nearest']),
            'method': lambda _: random.choice(['single', 'table']),
        },
        'isin': {
            'values': lambda _: random.choice([
                [random.randint(0, 10) for _ in range(random.randint(1, 5))],
                {'column_name': [random.randint(0, 10) for _ in range(random.randint(1, 5))]},
                pd.Series([random.randint(0, 10) for _ in range(random.randint(1, 5))]),
                pd.DataFrame({'column_name': [random.randint(0, 10) for _ in range(random.randint(1, 5))]})
            ])
        },
        'join': {
            'other': lambda df: random.choice([df for _ in range(10)]),
            'how': lambda _: random.choice(['left', 'right', 'outer', 'inner', 'cross']),
            'lsuffix': lambda _: random.choice(['_left', '_x']),
            'rsuffix': lambda _: random.choice(['_right', '_y']),
            'sort': lambda _: random.choice([True, False]),
        },
        'applymap': {
            'func': lambda _: random_function,
            'na_action': lambda _: random.choice([None, 'ignore']),
        },
        'apply': {
            'func': lambda _: random_function,
            'axis': lambda _: random.choice([0, 1, 'index', 'columns']),
            'raw': lambda _: random.choice([True, False]),
            'result_type': lambda _: random.choice(['expand', 'reduce', 'broadcast', None]),
        },
        'diff': {
            'periods': lambda _: random.choice([1, 2, 3, 4, 5]),
            'axis': lambda _: random.choice([0, 1, 'index', 'columns']),
        },
        'combine': {
            'other': lambda df: random.choice([df for _ in range(10)]),
            'func': lambda _: np.minimum,
            'fill_value': lambda _: random.choice([None, 0, 1, 10]),
            'overwrite': lambda _: random.choice([True, False]),
        },
    }

    def __init__(self, df, method, args, method_configs=None):
        self.df = df
        self.method = method
        self.args = args
        self.method_configs = method_configs if method_configs is not None else self.DEFAULT_METHOD_CONFIGS

    def mutate(self):
        self.df = self.mutate_dataframe(self.df)  # Assuming mutate_dataframe is a method
        self.args = {}
        self.method = random.choice(list(self.method_configs.keys()))
        method_config = self.method_configs.get(self.method, {})
        for arg, value_generator in method_config.items():
            self.args[arg] = value_generator(self.df)

    def mutate_dataframe(self, df):
        # Implementation of mutate_dataframe
        return df

    def __str__(self):
        args_str = ', '.join(f'{k}={v}' for k, v in self.args.items())
        return f"DataFrameMethodArgs({self.df}, method={self.method}, args={{{args_str}}})"

    def to_dict(self):
        # Convert main DataFrame to JSON
        df_json = self.df.to_json()

        # Convert DataFrames, Series, and functions within the args dictionary to JSON
        args = {}
        for key, value in self.args.items():
            if isinstance(value, pd.DataFrame):
                args[key] = {'is_dataframe': True, 'is_series': False, 'is_function': False, 'data': value.to_json()}
            elif isinstance(value, pd.Series):
                args[key] = {'is_dataframe': False, 'is_series': True, 'is_function': False, 'data': value.to_json()}
            elif callable(value):
                serialized_function = dill.dumps(value).hex()
                args[key] = {'is_dataframe': False, 'is_series': False, 'is_function': True, 'data': serialized_function}
            else:
                args[key] = {'is_dataframe': False, 'is_series': False, 'is_function': False, 'data': value}

        content = {
            'df': df_json,
            'method': self.method,
            'args': args
        }

        return content

    @staticmethod
    def from_dict(data_dict):
        """Builds the object from a dictionary."""
        # Convert main DataFrame from JSON
        df = pd.read_json(data_dict['df'])

        # Convert DataFrames, Series, and functions within the args dictionary from JSON
        args = {}
        for key, value in data_dict['args'].items():
            if value['is_dataframe']:
                args[key] = pd.read_json(value['data'])
            elif value['is_series']:
                args[key] = pd.read_json(value['data'], typ='series')
            elif value['is_function']:
                serialized_function = bytes.fromhex(value['data'])
                args[key] = dill.loads(serialized_function)
            else:
                args[key] = value['data']

        method = data_dict['method']
        method_configs = data_dict.get('method_configs', DataFrameMethodArgs.DEFAULT_METHOD_CONFIGS)
        return DataFrameMethodArgs(df, method, args, method_configs)