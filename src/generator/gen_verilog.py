'''
This file accepts a json file as input and generates a 
'''

import sys, json, struct, re

def get_bin_from_int(num):
    return bin(struct.unpack('!i',struct.pack('!f',float(num)))[0])

def write_comp_unit(f, conds, name):
    if (conds[1] == '>'):
        f.write('  fp_gt {}(.out({}), .f1({}), .f2({}));\n'.format(name+"_c", name, conds[0], conds[2]))
    else:
        f.write('  fp_gt {}(.out({}), .f1({}), .f2({}));\n'.format(name+"_c", name, conds[2], conds[0]))

def write_verilog(v_file, data, name):
    v_file.write('`include "../../fpu/fp_gt.v"\n\n')

    inputs = ""
    for i in range(len(data["Signals"])):
        inputs += ', input [31:0] {}'.format(data["Signals"][i])
    v_file.write('module {}(output out1, output out2{});\n'.format(name.split(".")[0].split("/")[-1], inputs))
    
    v_file.write("  reg out1 = 1'b0;\n")
    v_file.write("  reg out2 = 1'b1;\n")

    for k, v in data["Constants"].items():
        b = get_bin_from_int(v)
        v_file.write("  reg [31:0] {} = 32'b{};\n".format(k, b[2:].zfill(32)))

    v_file.write("\n")


    for k, v in data["Buy"]["Conditions"].items():
        v_file.write("  wire {}_b;\n".format(k))

    for k, v in data["Sell"]["Conditions"].items():
        v_file.write("  wire {}_s;\n".format(k))

    v_file.write("\n")

    for k, v in data["Buy"]["Conditions"].items():
        write_comp_unit(v_file, v, k+"_b")

    v_file.write("\n")

    for k, v in data["Sell"]["Conditions"].items():
        write_comp_unit(v_file, v, k+"_s")

    d_list = ['(', ')', '!', '|', '&', '^']
    
    buy_logic = data["Buy"]["Logic"].split(" ")
    for i in range(len(buy_logic)):
        if buy_logic[i] not in d_list:
            buy_logic[i] += "_b"
    s = ""
    buy_logic = s.join(buy_logic)

    sell_logic = ""
    sell_logic = data["Sell"]["Logic"].split(" ")
    for i in range(len(sell_logic)):
        if sell_logic[i] not in d_list:
            sell_logic[i] += "_s"
    s = ""
    sell_logic = s.join(sell_logic)

    v_file.write("\n")

    v_file.write('  always @ (*)\n')
    v_file.write('  begin\n')

    v_file.write('      if ({})\n'.format(sell_logic))
    v_file.write('      begin\n')
    v_file.write("          out1 = 1'b0;\n")
    v_file.write("          out2 = 1'b0;\n")
    v_file.write("      end\n")
    v_file.write("      else if ({})\n".format(buy_logic))
    v_file.write("      begin\n")
    v_file.write("          out1 = 1'b1;\n")
    v_file.write("          out2 = 1'b0;\n")
    v_file.write("      end\n")
    v_file.write("      else\n")
    v_file.write("      begin\n")
    v_file.write("          out1 = 1'b0;\n")
    v_file.write("          out2 = 1'b1;\n")
    v_file.write("      end\n")
    v_file.write("  end\n")
    v_file.write("endmodule")

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