import copy
original_dict = {'key1': ['value1'], 'key2': 'value2'}
deep_copied_dict = copy.deepcopy(original_dict)
original_dict['key1'].append('value3')
print(deep_copied_dict) 
print(original_dict)