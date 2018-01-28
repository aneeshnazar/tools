#!/usr/bin/env python3

import subprocess as sp
import sys

def gen_mf(name, compiler, files, srcdir, ext):
    return """NAME = %s
CC := %s
CFLAGS	+= -Wall -Wextra -Werror
SFILES = %s

ODIR = obj
SDIR = %s
SRC = $(addprefix $(SDIR)/,$(SFILES))
OBJ = $(addprefix $(ODIR)/,$(SFILES:%s=.o))
INC = includes/

$(ODIR)/%%.o: $(SDIR)/%s
	@$(CC) $(CFLAGS) -I $(INC) -c $^ -o $@

all: $(NAME)

$(NAME): $(OBJ)
	@$(CC) $(CFLAGS) -I $(INC) -o $@ $(OBJ)

$(OBJ): | $(ODIR)

$(ODIR):
	@mkdir $(ODIR)

clean:
	@rm -rf $(ODIR)

fclean: clean
	@rm -rf $(NAME)

re: fclean all""" % (name, compiler, files, srcdir, ext, "%"+ext)

def get_files(ext):
    return filter( lambda x:x.endswith(ext) ,sp.check_output(["ls", "-1"]).decode("utf-8").split('\n'))

def main():
    if (len(sys.argv) < 5):
        print ("Usage: ./generate_makefile.py [output directory] [compiler] [output binary name] [source directory] [source files]")
        exit(0);
    dir = sys.argv[1]
    compiler = sys.argv[2]
    name = sys.argv[3]
    srcdir = sys.argv[4]
    ext = '.' + sys.argv[5].split('.')[-1]
    files = "\t" + ' \\\n\t\t\t'.join(list(sys.argv[5:]))
    with open(dir + "Makefile", "w+") as mf:
        mf.write(gen_mf(name, compiler, files, srcdir, ext))

if __name__ == '__main__':
    main()
