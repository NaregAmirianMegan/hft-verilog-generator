`timescale 1ns / 1ps
`include "rsi.v"

module rsi_txt_in();
    reg [31:0] r_rsi;
    reg [31:0] ra_data[2:0];

    wire w_o1, w_o2;

    rsi uut (.out1(w_o1), .out2(w_o2), .RSI(r_rsi));

    integer i, f;
    initial begin
        f = $fopen("output.txt","w");
        $monitor("RSI=%d, OUT1=%b, OUT2=%b", r_rsi, w_o1, w_o2);
        $dumpfile("rsi_txt_in.vcd");
        $dumpvars(0, rsi_txt_in);

        $readmemh("data.hex", ra_data);
        
        for (i = 0; i < 3; i = i + 1)
        begin 
            r_rsi = ra_data[i];
            #1000;
            $fwrite(f,"RSI=%d, OUT1=%b, OUT2=%b\n", r_rsi, w_o1, w_o2);
            #1000;
        end
        $fclose(f); 
        $finish;
    end

endmodule