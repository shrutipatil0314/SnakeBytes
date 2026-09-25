import re
import string

message = "Hello , welcome to the world of regular expressions!"


class Pattern:
	"""Useful wrapper around Python's compiled regular-expression pattern."""

	def __init__(self, expression, flags=0):
		self._compiled = re.compile(expression, flags)

	@property
	def pattern(self):
		return self._compiled.pattern

	def search(self, text, pos=0, endpos=None):
		return self._compiled.search(text, pos, len(text) if endpos is None else endpos)

	def match(self, text, pos=0, endpos=None):
		return self._compiled.match(text, pos, len(text) if endpos is None else endpos)

	def fullmatch(self, text, pos=0, endpos=None):
		return self._compiled.fullmatch(text, pos, len(text) if endpos is None else endpos)

	def findall(self, text, pos=0, endpos=None):
		return self._compiled.findall(text, pos, len(text) if endpos is None else endpos)

	def finditer(self, text, pos=0, endpos=None):
		return self._compiled.finditer(text, pos, len(text) if endpos is None else endpos)

	def split(self, text, maxsplit=0):
		return self._compiled.split(text, maxsplit)

	def sub(self, replacement, text, count=0):
		return self._compiled.sub(replacement, text, count)

	def subn(self, replacement, text, count=0):
		return self._compiled.subn(replacement, text, count)


match_object = re.search("[0-9][0-9]", message)
print(match_object)  #* Check if a match object is returned (None if no match is found  )

house_number = "house number : 251/A"
match_object = re.search("[0-9][0-9]", house_number)
print(match_object)  # Check if a match object is returned (None if no match is found)

match_object = re.search("[0-9][0-9][0-9]", string="house number : 251/A")
print(match_object)  # Check if a match object is returned (None if no match is found)

#.
match_object = re.search("[0-9][0-9][0-9]", message)
print(match_object)  # Check if a match object is returned (None if no match is found)

match_object = re.search(pattern="[0-9][0-9][0-9]", string=message)
print(match_object)  # Check if a match object is returned (None if no match is found)  

match_object = re.search(pattern="[0-9][0-9]", string= "house number : 251/A")
print(match_object)  # Check if a match object is returned (None if no match is found)
