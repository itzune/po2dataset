#!/usr/bin/env python3

import os
import sys
import argparse
from .utils import (
    FORMAT_CHOICES,
    LICENSE_CHOICES,
    PLACEHOLDER_POLICIES,
    DEFAULT_LICENSE,
    DEFAULT_FORMAT,
    create_workdir,
    create_dataset,
    create_metadata,
    add_license,
    add_readme,
    make_zip,
)


def main():
    parser = argparse.ArgumentParser(description="Create a dataset from po files")

    parser.add_argument("path", type=str, help="Absolute po file path")
    parser.add_argument("--name", type=str, required=True, help="Source language code")
    parser.add_argument(
        "-s", "--source_code", type=str, required=True, help="Source language code"
    )
    parser.add_argument(
        "-t", "--target_code", type=str, required=True, help="Target language code"
    )
    parser.add_argument(
        "--ref", type=str, required=True, help="Reference of the source data"
    )
    parser.add_argument(
        "-o", "--output", type=str, required=False, help="Output file path"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=FORMAT_CHOICES,
        required=False,
        help="Extension name of the zip file",
    )

    parser.add_argument(
        "--license",
        type=str,
        choices=LICENSE_CHOICES,
        required=False,
        help="License file to be included in the package (select choice or provide custom file path)",
    )

    parser.add_argument(
        "--readme",
        type=str,
        required=False,
        help="Original README file to copy from",
    )

    parser.add_argument(
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
