# prepmd
**About:**
A python script to preprocess certain snippets of markdown.

Specifically used to process markdown in html before Jekyll applies markdown to post files. Used to get certain snippets in full html so that they may be enclosed in an html block.Small attempt to get around markdown's inability to be processed inside an html block.

**Requirements:**
 
 - Markdown.pl inside same dir.
 - Manual file name change inside the script (name the file you need preprocessed)

Tested for python 2.7+

**Usage:**

`python dev.py <file_name_here>`

Allows the use of multiple file inputs to each be processed individually

 1. input is a kramdown file (.md)
 2. mark off section for preprocessing betwen an html comment with '[**', '**]' used in between. Ex. <!-- [** ........**]-->
 3. Make sure Markdown.pl is in the same dir as both your .md file and prepmd
 4. change the name of 'exp' var in script to the name of your markdown file.
 5. run 'python prepmd.py'
 6. view 'yourInputFile_full.md' for the output file

**Goals:**

 1. Use a simplified method to create the output file
 2. turn overall script into a commandline tool format
 3. Restructure code to allow for multiple delimited markdown snippets to html
 4. Add self clean up for tmp files

