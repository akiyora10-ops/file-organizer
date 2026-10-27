"""Convert JSON to XML."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import xml.etree.ElementTree as ET


def dict_to_xml(tag: str, data) -> ET.Element:
    elem = ET.Element(tag)
    if isinstance(data, dict):
        for k, v in data.items():
            if k == "#text":
                elem.text = str(v)
            elif k == "@attributes":
                elem.attrib.update({kk: str(vv) for kk, vv in v.items()})
            elif isinstance(v, list):
                for item in v:
                    elem.append(dict_to_xml(k, item))
            else:
                elem.append(dict_to_xml(k, v))
    elif isinstance(data, list):
        for item in data:
            elem.append(dict_to_xml("item", item))
    else:
        elem.text = "" if data is None else str(data)
    return elem


def convert(text: str) -> str:
    obj = json.loads(text)
    if not isinstance(obj, dict) or len(obj) != 1:
        raise ValueError("JSON must be an object with a single root key")
    root_tag, data = next(iter(obj.items()))
    root = dict_to_xml(root_tag, data)
    return ET.tostring(root, encoding="unicode")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="JSON to XML.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-o", "--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    try:
        out = convert(text)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"error: {e}")
        return 1
    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
