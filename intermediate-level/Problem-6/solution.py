### Problem-6: Flatten a Nested JSON

def flatten_obj(obj: dict, parent_key: str = '') -> dict:
	new_obj = {}

	for key, val in obj.items():
		new_key = f"{parent_key}.{key}" if parent_key else key

		if isinstance(val, dict):
			new_obj.update(flatten_obj(val, new_key))
		else:
			new_obj[new_key] = val
	
	return new_obj

obj = {"a": {"b": 1}}
print(f"Flattened object: {flatten_obj(obj)}")