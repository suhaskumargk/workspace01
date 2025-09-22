
import os
import configparser


_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONFIG_PATH = os.path.join(_BASE_DIR, 'configs', 'config.ini')
config = configparser.ConfigParser()
config.read(_CONFIG_PATH)


class ConfigManager:

	@staticmethod
	def get(section: str, key: str):
		"""Get the value for a given section and key"""
		return config.get(section, key)

	@staticmethod
	def set(section: str, key: str, value: str):
		"""Set the value for a given section and key"""
		return config.set(section, key, value)

	@staticmethod
	def delete(section: str, key: str = None):
		"""Delete a key in a section, or delete a whole section if key is None."""
		if key is None:
			return config.remove_section(section)
		return config.remove_option(section, key)
