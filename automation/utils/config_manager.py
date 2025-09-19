
import configparser
import os
import tempfile
from typing import Optional, Dict


class ConfigManager:

	def __init__(self, path: Optional[str] = None):
		if path:
			self.path = path
		else:
			self.path = os.path.join('.', 'automation', 'configs', 'config.ini')
		self._parser = configparser.ConfigParser()
		self.load()

	def load(self) -> None:
		"""Load configuration from file. If file missing, create an empty one."""
		self._parser.read(self.path)

	def save(self) -> None:
		"""Save configuration to disk."""
		with open(self.path, 'w') as f:
			self._parser.write(f)

	def get(self, section: str, key: str) -> Optional[str]:
			if self._parser.has_section(section) and self._parser.has_option(section, key):
				return self._parser.get(section, key)
			return None

	def set(self, section: str, key: str, value: str) -> None:
		if not self._parser.has_section(section):
			self._parser.add_section(section)
		self._parser.set(section, key, value)
		self.save()

	def delete(self, section: str, key: Optional[str] = None) -> bool:
		"""Delete a key in a section, or delete a whole section if key is None."""
		if key is None:
			result = self._parser.remove_section(section)
		else:
			result = self._parser.remove_option(section, key)
		if result:
			self.save()
		return result
