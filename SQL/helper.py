import pandas


def read_csv(path_to_csv):
    return tuple(dict(item[1]) for item in tuple(pandas.read_csv(path_to_csv, sep=';', header=0, index_col = None).iterrows()))

def form_insert_from_dict_tuple(table_name, dict_tuple: [dict])->str:
    return f"INSERT INTO test.{table_name}({', '.join(dict_tuple[0].keys())}) VALUES {', '.join([str(tuple(i.values())) for i in dict_tuple])}"
