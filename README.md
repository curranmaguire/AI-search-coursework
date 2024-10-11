# AI Search Algorithms

This README provides instructions for setting up and running the AI search algorithms developed by Curran Maguire (cgmj52).

## Algorithms

This project implements two AI search algorithms:

1. Algorithm A: Genetic Algorithm (with enhancements)
2. Algorithm B: Ant Colony Optimisation

### Algorithm A: Enhanced Genetic Algorithm

The genetic algorithm has been enhanced using the following techniques:

1. Hybridization with 2-opt:
   - Improves the child generation process
   - Swaps non-adjacent edges and measures new tour weights
   - Saves optimal tours for the new population

2. Island-based grouping:
   - Uses different initial populations
   - Allows separate specialization of groups
   - Periodically swaps portions of populations between islands
   - Aims to reduce over-specialization and increase diversity

### Algorithm B: Ant Colony Optimisation

Standard implementation as covered in lectures.

## Installation

1. Download the project files.
2. Navigate to the project directory:
   ```
   cd cgmj52
   ```

## Usage

To run the AI search algorithms:

1. Ensure you are in the correct directory (`cgmj52`).
2. Run the code using your preferred method (e.g., Python interpreter).
3. When prompted, provide the path to your input text file.

Example:
```
python ai_search.py
Enter the path to your input file: /path/to/your/input.txt
```

## Input

The algorithm expects a text file as input. This file should contain the data for the problem you want to solve (e.g., city coordinates for a Traveling Salesman Problem). The ones used in the coursework are provided

## Output

The program will process the input file and provide search results based on the chosen algorithm's analysis.

## Notes

- Make sure you have the necessary dependencies installed before running the code.
- The enhanced genetic algorithm may require more computational resources due to its hybridization and island-based approach.

## Troubleshooting

If you encounter any issues:
- Double-check that you're in the correct directory (`cgmj52`).
- Verify that the input file path is correct and the file exists.
- Ensure you have the required permissions to read the input file and write to the output location.

For further assistance, please contact the developer (Curran Maguire)
