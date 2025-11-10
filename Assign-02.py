#!/usr/bin/env python3
"""
Pentagon Calculator

This script calculates the AREA and PERIMETER of a regular pentagon.

Minimum allowed values:
- Side length must be greater than 6.
- Apothem length must be greater than 4.5.

Usage (interactive): python3 Assign-02.py

Usage (non-interactive): python3 Assign-02.py -s 5 -a 3.5 -u cm

Author:
License: MIT
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate area and perimeter of a regular pentagon."
    )
    parser.add_argument("-s", "--side", type=float, help="side length of the pentagon")
    parser.add_argument(
        "-a", "--apothem", type=float, help="apothem length of the pentagon"
    )
    parser.add_argument(
        "-u", "--units", type=str, default="units", help="units (e.g., cm, m, in)"
    )
    return parser.parse_args()


def format_number(x):
    # Format the number to two decimal places for consistent output
    return f"{x:.2f}"


def calculate(side: float, apothem: float):
    """Return (area, perimeter) for a regular pentagon.

    Perimeter = 5 * side
    Area = 0.5 * perimeter * apothem  # standard formula for regular polygons
    """
    perimeter = 5.0 * side
    area = 0.5 * perimeter * apothem
    return area, perimeter


def interactive_input(prompt_text: str):
    try:
        return input(prompt_text)
    except (EOFError, KeyboardInterrupt):
        print()  # newline and exit gracefully
        sys.exit(1)


def main():
    args = parse_args()

    # If arguments not provided, ask interactively
    if args.side is None:
        while True:
            s_raw = interactive_input("Enter the side length of the pentagon: ")
            try:
                side = float(s_raw)
                if side <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive number for the side length.")
    else:
        side = args.side

    if args.apothem is None:
        while True:
            a_raw = interactive_input("Enter the apothem length of the pentagon: ")
            try:
                apothem = float(a_raw)
                if apothem <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive number for the apothem length.")
    else:
        apothem = args.apothem

    units = args.units

    # Validate side and apothem before calculation
    if side <= 0 or apothem <= 0:
        print("Error: Side and apothem must be positive numbers.")
        sys.exit(1)

    area, perimeter = calculate(side, apothem)

    # Output
    print("\n----- Results -----")
    print(f"Area of the pentagon: {format_number(area)} {units}^2")
    print(f"Perimeter of the pentagon: {format_number(perimeter)} {units}")
    print("--------------------")


if __name__ == "__main__":
    main()
