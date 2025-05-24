import json
import argparse
import os

def get_external_id(attack_pattern):
    for ref in attack_pattern.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            return ref.get("external_id", "")
    return ""

def get_tactics(attack_pattern):
    return ", ".join([p["phase_name"].replace("-", " ").title() for p in attack_pattern.get("kill_chain_phases", [])])

def extract_data_sources(obj):
    return obj.get("x_mitre_data_sources", [])

def extract_platforms(obj):
    return ", ".join(obj.get("x_mitre_platforms", []))

def extract_refs(obj):
    refs = []
    for ref in obj.get("external_references", []):
        url = ref.get("url")
        name = ref.get("description") or ref.get("source_name")
        if url:
            refs.append(f"- [{name}]({url})")
    return "\n".join(refs)

def format_markdown(obj):
    ext_id = get_external_id(obj)
    title = f"{ext_id} - {obj.get('name')}"
    tactics = get_tactics(obj)
    platforms = extract_platforms(obj)
    revoked = str(obj.get("revoked", False))
    subtech = str(obj.get("x_mitre_is_subtechnique", False))
    version = obj.get("x_mitre_version", "")


    md = f"# {title}\n\n"
    md += f"**ID:** {ext_id}  \n"
    md += f"**Tactic(s):** {tactics}  \n"
    md += f"**Platform(s):** {platforms}  \n"
    md += f"**Revoked:** {revoked}  \n"
    md += f"**Sub-technique:** {subtech}  \n"
    md += f"**Version:** {version}\n\n"
    md += f"## Description\n{obj.get('description', '')}\n\n"
    md += f"## Detection\n{obj.get('x_mitre_detection', '')}\n\n"

    data_sources = extract_data_sources(obj)
    if data_sources:
        md += "## Data Sources\n" + "\n".join([f"- {src}" for src in data_sources]) + "\n\n"

    refs = extract_refs(obj)
    if refs:
        md += f"## References\n{refs}\n"

    return md

def main():
    parser = argparse.ArgumentParser(description="Convert MITRE ATT&CK JSON to Markdown")
    parser.add_argument("input_json", help="Path to the STIX JSON bundle")
    parser.add_argument("output_md", help="Path to output .md file")
    args = parser.parse_args()

    with open(args.input_json, "r", encoding="utf-8") as f:
        bundle = json.load(f)

    attack_patterns = [obj for obj in bundle.get("objects", []) if obj.get("type") == "attack-pattern"]

    with open(args.output_md, "w", encoding="utf-8") as out_file:
        for obj in attack_patterns:
            out_file.write(format_markdown(obj))
            out_file.write("\n\n---\n\n")

    print(f"Markdown written to {args.output_md}")

if __name__ == "__main__":
    main()
