import curlconverter
import requests


def curl_to_requests(curl_command: str) -> str:
	return curlconverter.to_python(curl_command)

def main():
	
	print("Paste your cURL command from chrome and hit enter: ")
	# get input
	lines = []
	while True:
		line = input()
		if line == "":
			break
		lines += line

	lines[0] = ""
	command = '\\n'.join(lines)
	request = curl_to_requests(command)


if __name__ == '__main__':
	main()