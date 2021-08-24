import re

def camel_to_snake(name):
	name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name).lower()
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def format_movie_data(dic_data):
	data = dict((camel_to_snake(k), None if v == 'N/A' else v) for k,v in dic_data.items())

	if data.get('year'):
		year = data.get('year')
		year_range = year.split('–')
		start_year = year_range[0]
		end_year = None
		
		if len(year_range) > 1 and year_range[1] != '':
			end_year = year_range[1]
	
	data.pop('year')
	data['start_year'] = start_year
	data['end_year'] = end_year
	
	return data