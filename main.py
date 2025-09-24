import time
import pyperclip
import re
import sys
import subprocess
from urllib.parse import quote
import random

class CommentCurlRequest:

	def __init__(self, command: str):
		self.raw_command = command
		self.command_lines = command.split('\\\n')

		if len(self.command_lines) != 27:
			print("Error: command should have 27 lines")
			sys.exit(1)

		print("Successfully read command.")

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

		return self._send_request()

	def _send_request(self):
		command = ' '.join(self.command_lines)
		result = subprocess.run(command, shell=True, capture_output=True, text=True)
		return result.stdout


# class RandomEmojis():
# 	emojis = ["🔥", "🙏", "❤️", "🙌", "🫶", "🏔️"]

# 	def __init__(self):
# 		self.current_emoji = random.randint(0, len(RandomEmojis.emojis))
	
# 	def generate_comment(self):
# 		val = self.current_emoji * random.randint(1, 7)
# 		if random.random() < 0.2:
# 			self.current_emoji = random.randint(0, len(RandomEmojis.emojis))
# 		return val


SWITCH_COMMENT_PROBABILITY = 0.15
MIN_REQUEST_TIME_THRESHOLD_MS = 600
LOOP_ITERATIONS = 5000
MAX_CONSECUTIVE_WARNINGS = 5


def main():
	
	print("Copy your cURL command from Chrome, then come back and hit enter: ")
	_ = input()
	
	# get input
	command = pyperclip.paste()
	curl_request = CommentCurlRequest(command)

	# get random comments
	print("\nEnter a bunch of random comments to avoid making it look like you're a bot.")
	print("Make it look realistic by using emojis and random letters that you would type if you were on your phone spamming comments")
	print("The bot will repeat the comments a random amount of times and then switch to a different comment.")
	print("\nWhen you're done, just press enter again\n")

	comments = []
	c = input("Comment  0: ")
	while c != "":
		comments.append(c)
		c = input(f"Comment {len(comments):2}: ")

	# send comments
	consecutive_warnings = 0
	comment_idx = random.randint(0, len(comments) - 1)
	i = 0
	while i < LOOP_ITERATIONS:
		comment = comments[comment_idx]
		print(f"{i + 1: 4} Commenting \"{comment}\" ... ", end="", flush=True)

		start = time.perf_counter() * 1000
		result = curl_request.comment(comment)
		end = time.perf_counter() * 1000

		if (end - start) < MIN_REQUEST_TIME_THRESHOLD_MS: 
			print("Warning: request time was too short. This might mean the comment didn't go through")
			consecutive_warnings += 1
		elif result == "200":
			consecutive_warnings = 0
			print("success")
		else:
			print(f"Error {result}")
			break

		if random.random() < SWITCH_COMMENT_PROBABILITY:
			comment_idx = random.randint(0, len(comments) - 1)
		
		if consecutive_warnings > MAX_CONSECUTIVE_WARNINGS:
			print("Too many short requests in a row, comments are probably not going through. Time to switch accounts and try again!")
			break

		i += 1

	print(f"Commented {i} times")
	print("If you get error 302, try switching accounts and trying again")
		
	
if __name__ == '__main__':
	main()