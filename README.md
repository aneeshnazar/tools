# tools

An assortment of random scripts I've written to make my coding life easier.

## generate_class.py

I use this script to generate C++ class files - headers and implementations - from file names and variables.
The generated files are in Coplien's form - default constructor, copy constructor, destructor, and overloaded
assignment operator - as well as getters and setters for each class member.

## generate_makefile.py

I use this script to generate a makefile. The script takes in four-plus command-line arguments - the output directory, compiler type, name of the output file, and all of the source files. The script uses the file extension of the first-listed source file to generate object files, so be careful not to delete code!

## random_name_generator.py

I used this script to generate a list of random names. I do this by sending a GET request to an online random name generator,
then scraping the HTML output for the generated name.
