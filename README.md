Please create Python code which will take two input files, both files consist of alphabetically sorted ASCII lines, and will produce two outputs: - The first output file should contain lines that are present in the first input file but not in the second input file. - The second output file should contain lines that are present in the second input file but not in the first input file.

## Solution
### Pointers
* read the files 1 line at a time, if line1 is greater than line2 we know no line can match line2, thus we output line2 to output2
* same logic for line1 to output1
* time complexity: Since we're iterating over every line exactly 1 time we will have a complexity of O(N)
* space complexity: since we only read records 1 row at a time the space will be O(1)
