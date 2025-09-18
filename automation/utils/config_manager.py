
import configparser
import os
import tempfile
from typing import Optional, Dict


class ConfigManager:

	def __init__(self, path: Optional[str] = None):
		if path:
			self.path = path
		else:
			self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs', 'config.ini')
		self._parser = configparser.ConfigParser()
		self.load()

	def load(self) -> None:
		"""Load configuration from file. If file missing, create an empty one."""
		if not os.path.exists(self.path):
			os.makedirs(os.path.dirname(self.path), exist_ok=True)
			with open(self.path, 'w') as f:
				f.write('')
		self._parser.read(self.path)

	def save(self) -> None:
		"""Save configuration atomically to disk."""
		dirpath = os.path.dirname(self.path)
		os.makedirs(dirpath, exist_ok=True)
		fd, tmp_path = tempfile.mkstemp(dir=dirpath)
		try:
			with os.fdopen(fd, 'w') as tmpfile:
				self._parser.write(tmpfile)
			os.replace(tmp_path, self.path)
		finally:
			if os.path.exists(tmp_path):
				try:
					os.remove(tmp_path)
				except Exception:
					pass

	def get(self, section: str, key: str, fallback: Optional[str] = None) -> Optional[str]:
		return self._parser.get(section, key, fallback=fallback) if self._parser.has_section(section) else fallback

	def set(self, section: str, key: str, value: str) -> None:
		if not self._parser.has_section(section):
			self._parser.add_section(section)
		self._parser.set(section, key, value)
		self.save()

	def delete(self, section: str, key: Optional[str] = None) -> bool:
		"""Delete a key in a section, or delete a whole section if key is None."""
		if key is None:
			if self._parser.has_section(section):
				self._parser.remove_section(section)
				self.save()
				return True
			return False
		else:
			if self._parser.has_section(section) and self._parser.remove_option(section, key):
				self.save()
				return True
			return False

	def as_dict(self) -> Dict[str, Dict[str, str]]:
		"""Return the config as a nested dict: {section: {key: value}}"""
		return {s: dict(self._parser.items(s)) for s in self._parser.sections()}
