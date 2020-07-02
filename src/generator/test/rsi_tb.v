`timescale 1ns / 1ps
`include "rsi.v"

module rsi_tb();
   reg [31:0] RSI;
   reg [31:0] data[2:0];

   wire w_o1, w_o2;
   rsi uut (.out1(w_o1), .out2(w_o2), .RSI(RSI));

   integer i, f;
   initial begin
       f = $fopen("rsi_out.txt", "w");
       $monitor("RSI=%d, OUT1=%b, OUT2=%b", RSI, w_o1, w_o2);
       $dumpfile("rsi.vcd");
       $dumpvars(0, rsi_tb);

       $readmemh("data.hex", data);

       for (i = 1; i <= 2; i = i + 1)
       begin
           RSI = data[i+0];
           #1000;
           $fwrite(f, "RSI=%d, OUT1=%b, OUT2=%b", RSI, w_o1, w_o2);
           #1000;
       end
       $fclose(f);
       $finish;
   end
endmodule