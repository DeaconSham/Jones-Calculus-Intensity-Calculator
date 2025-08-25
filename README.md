# Jones Calculus Intensity Calculator

A Python script that uses the `sympy` library to symbolically calculate the intensity of polarized light after it passes through a generic optical element. The calculation is based on the Jones calculus formalism used in optics.

The script prompts the user for an initial (prepared) polarization state and a final (projected) polarization state. It then outputs the mathematical expression for the resulting intensity in terms of the optical element's physical properties (`phi1`, `phi2`, `r`).

## Background

In optics, the **Jones calculus** is a mathematical framework used to describe the polarization of light.

*   **Jones Vectors:** The polarization state of light is represented by a 2x1 vector (a Ket, `|ψ⟩`).
*   **Jones Matrices:** Optical elements (like polarizers, waveplates, or liquid crystals) are represented by 2x2 matrices (`J`).
*   **Transformation:** When light passes through an element, its new state is found by multiplying its Jones vector by the element's Jones matrix: `|ψ'⟩ = J|ψ⟩`.
*   **Intensity:** The final intensity measured by a detector is proportional to the squared magnitude of the projection of the final state onto the detector's state (a Bra, `⟨ϕ|`). The script calculates this value, which is proportional to the intensity: `I ∝ |⟨ϕ|J|ψ⟩|²`.

## Features

*   **Symbolic Mathematics:** Leverages `sympy` to provide exact mathematical expressions, not numerical approximations.
*   **Standard Polarization States:** Pre-defines the six standard basis states:
    *   Linear: Horizontal (H), Vertical (V)
    *   Diagonal: Diagonal (D), Anti-diagonal (A)
    *   Circular: Right (R), and Left (L)
*   **Generalized Jones Matrix:** Implements a customizable Jones matrix `J` dependent on three symbolic variables (`phi1`, `phi2`, `r`), allowing it to model a wide range of optical elements.
*   **Interactive:** A simple command-line interface asks the user to specify the initial and final states for the calculation.
*   **Formatted Output:** Uses `sympy`'s pretty-printing to display the final formula in a clean, readable format.

## Prerequisites

*   Python 3
*   SymPy library

## Installation

1.  Ensure you have Python 3 installed on your system.
2.  Install the SymPy library using pip:
    ```sh
    pip install sympy
    ```

## Usage

1.  Save the code as a Python file (e.g., `jones_calculator.py`).
2.  Run the script from your terminal:
    ```sh
    python jones_calculator.py
    ```
3.  The script will prompt you to enter the projection (final) and preparation (initial) polarization states. Use the single-letter abbreviations shown in the prompt.
