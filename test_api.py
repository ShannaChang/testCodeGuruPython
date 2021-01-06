import requests

seconds = []
i=0

while (i <10):
	response = requests.get('https://6n0jcdq0dh.execute-api.us-east-1.amazonaws.com/default/the-rds-proxy-rdsProxyHandlerDA266FA9-RG290KUOUTUM')
	seconds.append(response.elapsed.total_seconds())

print seconds

