# Optional function to change column name format from CamelCase to snake_case
def snakify(camel_list):
    snake_list = []
    for c in camel_list:
        underscored = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', c)
        refined = re.sub('([a-z0-9])([A-Z])', r'\1_\2', underscored).lower()
        snake_list.append(refined)
    return snake_list

# tt.columns = snakify(tt.columns)
