
from __future__ import annotations
import os
from typing import Any
import pandas as pd

def read_table(path: str, sheet_name=0) -> pd.DataFrame:
	if not os.path.exists(path):
		raise FileNotFoundError(f"File not found: {path}")
	lower = path.lower()
	if lower.endswith((".xls", ".xlsx")):
		return pd.read_excel(path, sheet_name=sheet_name)
	raise ValueError("Unsupported file type. Use .xls or .xlsx")


def write_table(df: pd.DataFrame, path: str, sheet_name: str = "Sheet1", index: bool = False) -> None:
	out_dir = os.path.dirname(os.path.abspath(path))
	if out_dir:
		os.makedirs(out_dir, exist_ok=True)
	lower = path.lower()
	if lower.endswith((".xls", ".xlsx")):
		with pd.ExcelWriter(path, engine="openpyxl") as writer:
			df.to_excel(writer, index=index, sheet_name=sheet_name)
		return
	raise ValueError("Unsupported file type. Use .xls or .xlsx")


def append_row(path: str, row: Any, sheet_name: str = "Sheet1") -> None:
	if isinstance(row, dict):
		new = pd.DataFrame([row])
	else:
		new = pd.DataFrame([row])
	if os.path.exists(path):
		df = read_table(path, sheet_name=sheet_name)
		df = pd.concat([df, new], ignore_index=True)
		write_table(df, path, sheet_name=sheet_name)
		return
	write_table(new, path, sheet_name=sheet_name)


def update_cell(path: str, row_index: int, column: Any, value: Any, sheet_name: str = "Sheet1") -> None:
	df = read_table(path, sheet_name=sheet_name)
	try:
		df.at[row_index, column] = value
	except Exception:
		df.iat[row_index, int(column)] = value
	write_table(df, path, sheet_name=sheet_name)


__all__ = ["read_table", "write_table", "append_row", "update_cell"]


def save_table(data, out_path: str, columns=None, index: bool = False, excel_sheet_name: str = "Sheet1"):
	if isinstance(data, pd.DataFrame):
		write_table(data, out_path, sheet_name=excel_sheet_name, index=index)
		return out_path
	try:
		df = pd.DataFrame.from_records(list(data))
	except Exception:
		df = pd.DataFrame(data, columns=columns)
	write_table(df, out_path, sheet_name=excel_sheet_name, index=index)
	return out_path


__all__.append("save_table")


