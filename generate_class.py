#!/usr/bin/env python3

import sys

def gen_header(h_name, name, var_names, var_types):
    header = """#ifndef %s_H
#define %s_H

class %s {
    private:
""" % (h_name, h_name, name)

    body = """\tpublic:
        %s ();
        %s (%s const &cc);
        ~%s ();
        %s &operator=(%s const &input);

""" % (name, name, name, name, name, name)

    for i in range(len(var_names)):
        header += "\t\t" + var_types[i] + " " + var_names[i].strip() + ";\n"
        body += "\t\t" + var_types[i] + " get" + var_names[i].strip().title() + "(void) const;\n"
        body += "\t\t" + "void set" + var_names[i].strip().title() + "(" + var_types[i] + " _" + var_names[i].strip() + ");\n"

    footer = """};
#endif
    """
    return (header + body + footer)

def gen_imp(name, var_names, var_types):
    body = """#include "%s.Class.hpp"

%s::%s(){}

%s::%s(%s const &cc)
{
    *this = cc;
}

%s::~%s(){}

%s &%s::operator=(%s const &input)
{
""" % (name, name, name, name, name, name, name, name, name, name, name)

    eq = """\treturn (*this);
}

"""

    for i in range(len(var_names)):
        body += "\t" + var_names[i].strip() + " = input." + var_names[i].strip() + ";\n"
        eq += var_types[i] + " " + name + "::get" + var_names[i].strip().title() + "(void) const { return " + var_names[i].strip() + ";}\n\n"
        eq += "void " + name + "::set" + var_names[i].strip().title() + "(" + var_types[i] + " _" + var_names[i].strip() + "){" + var_names[i].strip() + " = _" + var_names[i].strip() + ";}\n\n"

    return body + eq

def main():
    if (len(sys.argv) != 2):
        print ("Usage: ./generate_class.py [output directory]")
        exit(0);
    var_types = []
    var_names = []
    name = input()
    h_name = name.upper()
    while True :
        input_ = sys.stdin.readline()
        if input_ == '':
            break
        var_names.append(input_.split(' ')[1])
        var_types.append(input_.split(' ')[0])

    impfile = gen_imp(name, var_names, var_types)

    headerfile = gen_header(h_name, name, var_names, var_types)

    with open(sys.argv[1] + name + ".Class.hpp", 'w+') as header:
        header.write(headerfile)
    with open(sys.argv[1] + name + ".Class.cpp", 'w+') as imp:
        imp.write(impfile)

if __name__ == '__main__':
    main()
