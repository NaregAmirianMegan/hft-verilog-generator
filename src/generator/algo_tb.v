`timescale 1ns / 1ps
`include "algo.v"

module algo_tb();
   reg [31:0] time_;
   reg [31:0] price_;
   reg [31:0] data[4:0];

   wire w_o1, w_o2;
   algo uut (.out1(w_o1), .out2(w_o2), .time_(time_), .price_(price_));

   integer i, f;
   initial begin
       f = $fopen("algo_out.txt", "w");
       $monitor("time_=%d, price_=%d, OUT1=%b, OUT2=%b", time_, price_, w_o1, w_o2);
       $dumpfile("algo.vcd");
       $dumpvars(0, algo_tb);

       $readmemh("data.hex", data);
