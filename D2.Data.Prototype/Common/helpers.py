def replace_dashes(obj: dict):
	return {key.replace("-", "_"): value for key, value in obj.items()}


def dict_to_list(data: dict):
	return [*data.items()]