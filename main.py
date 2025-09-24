import requests
import pyperclip
import re
import subprocess
from urllib.parse import quote

class CommentCurlRequest:

	def __init__(self, command: str):
		self.raw_command = command
		self.command_lines = command.split('\\\n')
		self.command_lines[0] = "curl -o /dev/null -s -w \"%{http_code}\" 'https://www.instagram.com/graphql/query'"
		self.data_raw = self.command_lines[-1]

	
	def print_command_lines(self):
		for l in self.command_lines:
			print(l)
		
	def print_data_raw(self):
		print(self.data_raw)
	
	# this is the goal
	def comment(self, comment: str):
		search_re = r"(%7B%22comment_text%22%3A%22).*?(%22)"
		replace_re = r"\1" + quote(comment) + r"\2"

		# replace comment text
		self.command_lines[-1] = re.sub(
			search_re,
			replace_re,
			self.data_raw,
			flags=re.DOTALL
		)

		self._send_request()

	def _send_request(self):
		command = ' '.join(self.command_lines)
		result = subprocess.run(command, shell=True, capture_output=True, text=True)
		print(result.stdout)



def main():
	
	print("Copy your cURL command from chrome and hit enter: ")
	_ = input()
	
	# get input
	command = pyperclip.paste()
	curl_request = CommentCurlRequest(command)
	curl_request.comment("SCO 1")




if __name__ == '__main__':
	main()