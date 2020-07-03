`timescale 1ns / 1ps
`include "fp_gt.v"

module fp_txt_in();
    reg [31:0] F1;
    reg [31:0] F2;
    reg [31:0] data[5:0];

    wire RESULT;

    fp_gt uut (.out(RESULT), .f1(F1), .f2(F2));

    integer i;
    initial begin
        $monitor("F1=%d, F2=%d, RESULT=%b", F1[30:0], F2[30:0], RESULT);
        $dumpfile("fp_txt_in.vcd");
        $dumpvars(0, fp_txt_in);

        $readmemh("data.hex", data);
        
        for (i = 0; i < 6; i = i + 2)
        begin 
            F1 = data[i];
            F2 = data[i+1];
            #1000;
        end
        $finish;
    end

endmodule