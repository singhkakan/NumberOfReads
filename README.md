# NumberOfReads
A python script that reads a fastQ file (in txt format) and returns the length of reads

To use the script, head the required number of lines of a fastq file into a txt file.
The script will take the txt file name as input, count the number of nucleotides in each read
and output the results (separated by a newline) in a text file.

The output text file can be converted to csv and loaded in R to generate plots.

This approach can help you visualize the distribution of read lengths in any of your samples, at any stage of analysis. 
