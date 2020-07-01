'''
This file accepts a json file as input and generates a 
'''

import sys, json

def write_verilog(v_file, data, name):
    v_file.write('`include "fp_gt.v"\n\n')

    inputs = ""
    for i in range(len(data["Signals"])):
        inputs += ', input [31:0] {}'.format(data["Signals"][i])
    v_file.write('module {}(output out1, output out2{});\n'.format(name.split(".")[0].split("/")[-1], inputs))
    
    v_file.write("  reg out1 = 1'b1;\n")
    v_file.write("  reg out2 = 1'b0;\n")






def main(file, name):
    data, v_file = None, None
    try:
        with open(file) as f:
            data = json.load(f)
    except:
        print("Error: couldn't open json file, ensure path is correct.")
        sys.exit()
    try:
        v_file = open(name, "w")
    except:
        print("Error: couldn't create .v file, ensure file name doesn't use odd characters.")
        sys.exit()

    write_verilog(v_file, data, name)

def display_help():
    print("Help: (must be using > python 3.6.*)")
    print("[python gen_verilog.py --help], for help")
    print("[python gen_verilog.py file.json], to create .v with same name as json")
    print("[python gen_verilog.py -o example.v file.json], to create .v file with name 'example.v'")
    sys.exit()

if __name__ == "__main__":
    assert len(sys.argv) == 4 or len(sys.argv) == 2, "Wrong number of args, use --help."
    if sys.argv[1] == "--help":
        display_help()
    
    json_file, json_name = None, None
    if len(sys.argv) == 4:
        json_file = sys.argv[3]
        json_name = sys.argv[2]
    else:
        json_file = sys.argv[1]
        json_name = sys.argv[1].split(".")[0]+".v"
    
    main(json_file, json_name)