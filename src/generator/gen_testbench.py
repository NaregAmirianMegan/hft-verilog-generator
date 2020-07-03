'''
This file takes a csv formatted input data file and an algorithm name and generates two files: 
a raw data file and a test bench in verilog used to run the the specified algorithm on the raw data file.
'''
import sys, csv, struct

def get_bin_from_int(num):
    return bin(struct.unpack('!i',struct.pack('!f',float(num)))[0])

def bin_to_hex(b):
    hexi = {"0000": 0, "0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5, "0110": 6, "0111": 7, "1000": 8, "1001": 9, "1010": 'a', "1011": 'b', "1100": 'c', "1101": 'c', "1110": 'e', "1111": 'f'}
    i = 0
    retstr = ""
    while i < 32:
        retstr += str(hexi[b[i:i+4]])
        i+=4
    return retstr

def gen_raw(csv_file, algo):
    fields = None
    try:
        with open(csv_file, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            i = 0
            data_file = open(csv_file.split(".")[0]+".hex", "w")
            for row in csv_reader:
                if i == 0:
                    fields = row
                    data_file.write(str(hex(len(row))[2:]))
                    data_file.write("\n")
                else:
                    for num in row:
                        b = get_bin_from_int(int(num))
                        b = b[2:].zfill(32)
                        b = bin_to_hex(b)
                        data_file.write(b)
                        data_file.write("\n")
                i += 1
        return fields, i
    except:
        print("Error: couldn't read csv file.")

def gen_tb(fields, rows, algo_v, data_csv):
    tb_name = algo_v.split(".")[0]+"_tb.v"
    with open(tb_name, "w") as f:
        f.write("`timescale 1ns / 1ps")
        f.write("\n")
        f.write('`include "{}"'.format(algo_v.split("/")[-1]))
        f.write("\n\n")

        f.write("module {}();\n".format(tb_name.split(".")[0].split("/")[-1]))

        args_list = ".out1(w_o1), .out2(w_o2)"
        mon_list = ""
        mon_args = ""
        for i in range(len(fields)):
            fields[i] = fields[i]
            f.write("   reg [31:0] {};\n".format(fields[i]))
            args_list += ", .{}({})".format(fields[i], fields[i])
            mon_list += fields[i] + "=%d, "
            mon_args += fields[i] + ", "

        f.write('   reg [31:0] data[{}:0];\n\n'.format(rows-1))

        f.write('   wire w_o1, w_o2;\n')
            
        f.write('   {} uut ({});\n\n'.format(algo_v.split(".")[0].split("/")[-1], args_list))

        f.write('   integer i, f;\n')
        f.write('   initial begin\n')

        f.write('       f = $fopen("{}_out.txt", "w");\n'.format(algo_v.split(".")[0].split("/")[-1]))

        f.write('       $monitor("{}OUT1=%b, OUT2=%b", {}w_o1, w_o2);\n'.format(mon_list, mon_args))

        f.write('       $dumpfile("{}.vcd");\n'.format(algo_v.split(".")[0].split("/")[-1]))

        f.write('       $dumpvars(0, {});\n\n'.format(tb_name.split(".")[0].split("/")[-1]))

        f.write('       $readmemh("{}", {});\n\n'.format(data_csv.split(".")[0]+".hex", "data"))

        f.write('       for (i = 1; i <= {}; i = i + {})\n'.format(str(rows-1), str(len(fields))))
        f.write('       begin\n')

        for i in range(len(fields)):
            f.write('           {} = data[i+{}];\n'.format(fields[i], str(i)))
            f.write('           #1000;\n')
        f.write('           $fwrite(f, "{}OUT1=%b, OUT2=%b{}{}", {}w_o1, w_o2);\n'.format(mon_list, "\\", "n", mon_args))
        f.write('           #1000;\n')

        f.write('       end\n')
        f.write('       $fclose(f);\n')
        f.write('       $finish;\n')

        f.write('   end\n')
        f.write('endmodule')



if __name__ == "__main__":
    assert len(sys.argv) == 3, "Oops, make sure you run $ python gen_testbench.py [path/to/data.csv] [path/to/algo_mod.v]"

    data_csv = sys.argv[1]
    algo_v = sys.argv[2]

    fields, rows = gen_raw(data_csv, algo_v)
    rows = 1 + (rows-1)*len(fields)
    #print(fields, rows)
    gen_tb(fields, rows, algo_v, data_csv)