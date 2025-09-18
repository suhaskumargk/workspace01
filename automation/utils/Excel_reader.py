
from __future__ import annotations

import os
from typing import Iterable, List, Mapping, Optional, Union

import pandas as pd


TableLike = Union[pd.DataFrame, Iterable[Mapping], Mapping[str, Iterable], Iterable[Iterable]]


def _normalize_to_df(data: TableLike, columns: Optional[List[str]] = None) -> pd.DataFrame:
	if isinstance(data, pd.DataFrame):
		return data.copy()

	# list/iterable of mappings like [{'a':1}, {'a':2}]
	try:
		# check first element safely
		iterator = iter(data)  # type: ignore[arg-type]
		first = next(iterator)
	except StopIteration:
		# empty iterable -> empty DataFrame with columns if provided
		return pd.DataFrame(columns=columns)
	except TypeError:
		# Not iterable as expected -> fallthrough to raise
		raise ValueError("Unsupported data type for save_table")

	# if first is a mapping, treat as records
	if isinstance(first, Mapping):
		# rebuild iterator including first
		records = [first] + list(iterator)
		return pd.DataFrame.from_records(records)

	# if first is an iterable (row)
	if isinstance(first, Iterable):
		rows = [list(first)] + [list(r) for r in iterator]
		return pd.DataFrame(rows, columns=columns)

	# fallback
	raise ValueError("Unsupported row element type for save_table")


def save_table(
	data: TableLike,
	out_path: str,
	columns: Optional[List[str]] = None,
	index: bool = False,
	excel_sheet_name: str = "Sheet1",
) -> str:
	"""Save tabular data to CSV or Excel using a single generic method.

	The output format is chosen from the file extension of `out_path`:
	  - .csv -> CSV
	  - .xls/.xlsx -> Excel (openpyxl)

	Args:
		data: table-like input (see module docstring).
		out_path: destination file path. Parent directories will be created.
		columns: optional column names (useful when data is list-of-lists).
		index: whether to write row index to file (default False).
		excel_sheet_name: sheet name when writing Excel files.

	Returns:
		The absolute path to the written file.

	Raises:
		ValueError for unsupported output extensions or input formats.
	"""

	df = _normalize_to_df(data, columns=columns)

	out_path = os.path.abspath(out_path)
	os.makedirs(os.path.dirname(out_path), exist_ok=True)

	lower = out_path.lower()
	if lower.endswith(".csv"):
		df.to_csv(out_path, index=index)
	elif lower.endswith(".xls") or lower.endswith(".xlsx"):
		# use pandas' ExcelWriter which will pick openpyxl
		with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
			df.to_excel(writer, index=index, sheet_name=excel_sheet_name)
	else:
		raise ValueError("Unsupported output extension, use .csv, .xls or .xlsx")

	return out_path

