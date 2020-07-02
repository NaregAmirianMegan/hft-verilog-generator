`timescale 1ns / 1ps
`include "test/test.v"

module test/test_tb();
   reg [31:0] rsi_;
   reg [31:0] data[2:0];

   wire w_o1, w_o2;
   test/test uut (.out1(w_o1), .out2(w_o2), .rsi_(rsi_));

   integer i, f;
   initial begin
       f = $fopen("test/test_out.txt", "w");
       $monitor("rsi_=%d, OUT1=%b, OUT2=%b", rsi_, w_o1, w_o2);
       $dumpfile("test/test.vcd");
       $dumpvars(0, test/test_tb);

       $readmemh("data.hex", data);

       for (i = 1; i < 2; i = i + 1)
       begin
           rsi_ = data[i+0];
           #1000;
           $fwrite(f, "rsi_=%d, OUT1=%b, OUT2=%b", rsi_, w_o1, w_o2));
           #1000;
       end
       $fclose(f);
       $finish;
   end
endmodule