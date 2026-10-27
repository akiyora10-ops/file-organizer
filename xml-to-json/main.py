"""Convert simple XML to JSON."""

from __future__ import annotations

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable


def xml_to_dict(elem: ET.Element):
    result = {}
    if elem.attrib:
        result["@attributes"] = elem.attrib
    children = list(elem)
    if children:
        for child in children:
            val = xml_to_dict(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(val)
            else:
                result[child.tag] = val
    else:
        text = (elem.text or "").strip()
        if elem.attrib:
            result["#text"] = text
        else:
            return text if text else None
    return result


def convert(text: str) -> str:
    root = ET.fromstring(text)
    return json.dumps({root.tag: xml_to_dict(root)}, indent=2, ensure_ascii=False)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="XML to JSON.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-o", "--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    try:
        out = convert(text)
    except ET.ParseError as e:
        print(f"xml error: {e}")
        return 1
    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
