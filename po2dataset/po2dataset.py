#!/usr/bin/env python3

import os
import sys
import re
import json
import zipfile
import shutil
import polib
import argparse
import requests

DEFAULT_FORMAT = "argosdata"
FORMAT_CHOICES = [DEFAULT_FORMAT, "zip"]

DEFAULT_LICENSE = "CC0"
LICENSE_MAPPING = {
    DEFAULT_LICENSE: "https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt",
    "CC-BY": "https://creativecommons.org/licenses/by/4.0/legalcode.txt",
    "CC-BY-SA": "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt",
}
LICENSE_CHOICES = [key for key, value in LICENSE_MAPPING.items()]

COMMON_PLACEHOLDERS = [
    r"\s*%[@sdf]",  # %@ %s %d and %f
    r"\s*%\w+%",  # %number%
    r"\s*%[\{\()]\w+[\}\)]",  # %{amount} and  %(amount)
    r"\s*[^%]\{{1,2}\w+\}{1,2}",  # {amount} and {{amount}}
    # "%1$s",
    # "%1$d",
    # "%2$s",
    # "%2$d",
    # "%3$s",
    # "%3$d",
    # "%4$s",
    # "%4$d",
]
DEFAULT_PLACEHOLDER_POLICY = "skip"
PLACEHOLDER_POLICIES = [
    DEFAULT_PLACEHOLDER_POLICY,  # Skips all strings containing placeholders in order to add to the final project
    "remove",  # Removes all placeholders from strings and adds those strings to the final project
    "do_nothing",
]


def create_workdir(output, name, source_code, target_code):
    try:
        path = os.path.join(
            output, "data-{}-{}_{}".format(name, source_code, target_code)
        )
        os.mkdir(path)
        print("Working directory '%s' created successfully" % path)
        return path
    except OSError as error:
        print(
            "Working directory '%s' can not be created. This folder already exists!"
            % path
        )
        sys.exit()


def find_placeholder(txt):
    for ph in COMMON_PLACEHOLDERS:
        x = re.search(ph, txt)
        if x:
            return x
    return False


def create_dataset(path, output, ph_policy="skip"):
    pofile = polib.pofile(path)
    total_strings = len(pofile)
    translated_strings = len(pofile.translated_entries())
    print("{} from {} strings to process".format(translated_strings, total_strings))

    f_source = open("{}/source".format(output), "w")
    f_target = open("{}/target".format(output), "w")
    procesed_strings = 0
    for i, entry in enumerate(pofile.translated_entries(), 1):
        msgid = entry.msgid
        msgstr = entry.msgstr
        if ph_policy == "skip" and find_placeholder(msgid):
            continue
        elif ph_policy == "remove":
            ph = find_placeholder(msgid)
            while ph:
                msgid = msgid.replace(ph.group(), "")
                ph = find_placeholder(msgid)
            ph = find_placeholder(msgstr)
            while ph:
                msgstr = msgstr.replace(ph.group(), "")
                ph = find_placeholder(msgstr)

        print(msgid, file=f_source)
        print(msgstr, file=f_target)
        process = (i / translated_strings) * 100
        print("%{:.0f} completed...".format(process), end="\r")
        procesed_strings += 1
    f_source.close()
    f_target.close()
    print("\n")
    return procesed_strings


def create_metadata(output, name, source_code, target_code, ref, total_strings):
    metadata = {
        "name": name,
        "type": "data",
        "from_code": source_code,
        "to_code": target_code,
        "size": total_strings,
        "reference": ref,
    }
    with open("{}/metadata.json".format(output), "w") as f:
        json.dump(metadata, f, indent=2)


def add_license(output, license=DEFAULT_LICENSE):
    print("Adding {} license to the package...".format(license))
    response = requests.get(LICENSE_MAPPING[license])
    if response.status_code == 200:
        with open("{}/LICENSE".format(output), "w") as f:
            f.write(response.text)
    else:
        print("Couldn't retrieve the license due to connection issues")


def add_readme(output, readme_path=None):
    if readme_path:
        print("Adding {} license to the package...".format(readme_path))
        basename = os.path.basename(readme_path)
        readme_output = os.path.join(output, basename)
        shutil.copyfile(readme_path, readme_output)
    else:
        print("Couldn't retrieve the README file")


def make_zip(output, format=DEFAULT_FORMAT):
    print("Creating {} file in {}".format(format, output))
    zip_path = "{}.{}".format(output, format)
    with zipfile.ZipFile(zip_path, "w") as zipf:
        # Direktorioan dauden fitxategi guztiak zip fitxategian sartuko ditugu
        for root, dirs, files in os.walk(output):
            for file in files:
                file_path = os.path.join(root, file)
                # Fitxategia zip fitxategira gehitu
                zipf.write(file_path, os.path.relpath(file_path, output))
    print("Clearing working directory")
    shutil.rmtree(output)


def main():
    parser = argparse.ArgumentParser(description="Create dataset from po file")

    parser.add_argument("path", type=str, help="Absolute po file path")
    parser.add_argument(
        "-n", "--name", type=str, required=True, help="Source language code"
    )
    parser.add_argument(
        "-s", "--source_code", type=str, required=True, help="Source language code"
    )
    parser.add_argument(
        "-t", "--target_code", type=str, required=True, help="Target language code"
    )
    parser.add_argument(
        "-r", "--ref", type=str, required=True, help="Reference of the source data"
    )
    parser.add_argument(
        "-o", "--output", type=str, required=False, help="Output file path"
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=FORMAT_CHOICES,
        required=False,
        help="Extension name of the zip file",
    )

    parser.add_argument(
        "-l",
        "--license",
        type=str,
        choices=LICENSE_CHOICES,
        required=False,
        help="License file to be included in the package (select choice or provide custom file path)",
    )

    parser.add_argument(
        "-re",
        "--readme",
        type=str,
        required=False,
        help="Original README file to copy from",
    )

    parser.add_argument(
        "-ph",
        "--ph-policy",
        type=str,
        choices=PLACEHOLDER_POLICIES,
        required=False,
        help="Policy to substract or skip placeholders in strings",
    )

    args = parser.parse_args()

    output = args.output or ""
    if output and not os.path.exists(output):
        print("{} output directory does not exist!!".format(output))
        sys.exit()

    output = create_workdir(output, args.name, args.source_code, args.target_code)

    string_count = create_dataset(args.path, output, args.ph_policy)
    create_metadata(
        output, args.name, args.source_code, args.target_code, args.ref, string_count
    )

    license = args.license or DEFAULT_LICENSE
    add_license(output, license)

    add_readme(output, args.readme)

    format = args.format or DEFAULT_FORMAT
    make_zip(output, format)

    print("Dataset created successfully!!")


if __name__ == "__main__":
    main()
