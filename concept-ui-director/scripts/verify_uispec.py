#!/usr/bin/env python3
"""
verify_uispec.py - Deterministic contract validator for .uispec specifications.
Usage:
    python3 verify_uispec.py --spec .uispec/specs/<name>.spec.md --slots .uispec/content/<name>.slots.md
"""

import argparse
import re
import sys
from pathlib import Path

FORBIDDEN_MOTION_PROPS = {"height", "width", "margin", "padding", "gap", "font-size", "top", "bottom", "left", "right"}
VALID_DESIGN_CLASSES = {"Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6"}

def parse_slots_file(slots_path: Path) -> dict:
    if not slots_path.exists():
        raise FileNotFoundError(f"Slots file not found: {slots_path}")
    
    slots = {}
    content = slots_path.read_text(encoding="utf-8")
    for line_num, line in enumerate(content.splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("CHANNEL:") or line.startswith("These values"):
            continue
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip()
            val = parts[1].strip().strip('"').strip("'")
            slots[key] = (val, line_num)
    return slots

def parse_spec_file(spec_path: Path) -> dict:
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec file not found: {spec_path}")
    
    content = spec_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    spec_data = {
        "design_class": None,
        "slot_keys": [],
        "text_node_budget": None,
        "decorative_budget": None,
        "motion_props": [],
        "errors": []
    }
    
    # Check Design Class
    class_match = re.search(r"UI Design Class:\s*(Class\s*[1-6])", content, re.IGNORECASE)
    if class_match:
        spec_data["design_class"] = class_match.group(1).title()
    
    # Check Element Budget
    text_node_match = re.search(r"Text Nodes:\s*(\d+)", content, re.IGNORECASE)
    if text_node_match:
        spec_data["text_node_budget"] = int(text_node_match.group(1))
    
    dec_match = re.search(r"Decorative Elements:\s*(\d+)", content, re.IGNORECASE)
    if dec_match:
        spec_data["decorative_budget"] = int(dec_match.group(1))

    # Parse Slot Table
    in_slot_table = False
    for line in lines:
        if "##" in line and "Slot Table" in line:
            in_slot_table = True
            continue
        if in_slot_table and line.startswith("##"):
            in_slot_table = False
            continue
        if in_slot_table and line.startswith("|") and not line.startswith("|---") and not "Slot Key" in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if cols and cols[0]:
                spec_data["slot_keys"].append(cols[0])

    # Parse Motion Table
    in_motion_table = False
    for line in lines:
        if "##" in line and "Motion" in line:
            in_motion_table = True
            continue
        if in_motion_table and line.startswith("##"):
            in_motion_table = False
            continue
        if in_motion_table and line.startswith("|") and not line.startswith("|---") and not "Element" in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 3:
                animated_props = cols[2].lower()
                spec_data["motion_props"].append(animated_props)
                for forbidden in FORBIDDEN_MOTION_PROPS:
                    if re.search(rf"\b{forbidden}\b", animated_props):
                        spec_data["errors"].append(
                            f"FORBIDDEN_MOTION_PROPERTY: '{forbidden}' is animated in motion table row: {line.strip()}"
                        )

    return spec_data

def main():
    parser = argparse.ArgumentParser(description="Deterministic .uispec contract validator.")
    parser.add_argument("--spec", required=True, help="Path to .uispec/specs/<name>.spec.md")
    parser.add_argument("--slots", required=True, help="Path to .uispec/content/<name>.slots.md")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    slots_path = Path(args.slots)

    errors = []
    warnings = []

    try:
        slots = parse_slots_file(slots_path)
    except Exception as e:
        print(f"❌ ERROR: Failed to parse slots file: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        spec = parse_spec_file(spec_path)
    except Exception as e:
        print(f"❌ ERROR: Failed to parse spec file: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Validate Design Class
    if not spec["design_class"] or spec["design_class"] not in VALID_DESIGN_CLASSES:
        errors.append(f"MISSING_DESIGN_CLASS: Spec must declare one of {VALID_DESIGN_CLASSES}")

    # 2. Validate Slot Keys in Slot File
    for key in spec["slot_keys"]:
        # Handle wildcard or range keys like list.preview (matches list.preview, list.1.preview, etc.)
        matched = False
        for slot_key in slots:
            if slot_key == key or slot_key.startswith(key.replace(".1", "")):
                matched = True
                break
        if not matched and key not in slots:
            errors.append(f"MISSING_SLOT_KEY: Key '{key}' referenced in spec table is not defined in {slots_path.name}")

    # 3. Validate Text Node Budget
    if spec["text_node_budget"] is not None and spec["slot_keys"]:
        slot_count = len(spec["slot_keys"])
        if spec["text_node_budget"] != slot_count:
            warnings.append(
                f"BUDGET_MISMATCH: Text Nodes budget ({spec['text_node_budget']}) does not match slot table row count ({slot_count})"
            )

    # 4. Include Motion Errors
    errors.extend(spec["errors"])

    # Output Results
    print("=" * 60)
    print(f"🔍 UISPEC CONTRACT VERIFICATION: {spec_path.name}")
    print(f"   Design Class: {spec.get('design_class', 'UNKNOWN')}")
    print(f"   Slots Tested: {len(spec['slot_keys'])} spec keys against {len(slots)} slot entries")
    print("=" * 60)

    if warnings:
        for w in warnings:
            print(f"⚠️  WARNING: {w}")

    if errors:
        for err in errors:
            print(f"❌ ERROR: {err}", file=sys.stderr)
        print("\n💥 CONTRACT VERIFICATION FAILED. Fix errors before handoff.")
        sys.exit(1)
    else:
        print("✅ ALL CONTRACT INVARIANTS PASSED. Spec is ready for implementer handoff.")
        sys.exit(0)

if __name__ == "__main__":
    main()
