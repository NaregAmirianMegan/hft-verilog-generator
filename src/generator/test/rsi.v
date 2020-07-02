`include "../../fpu/fp_gt.v"

module rsi(output out1, output out2, input [31:0] RSI);
  reg out1 = 1'b0;
  reg out2 = 1'b1;
  reg [31:0] low = 32'b01000001111100000000000000000000;
  reg [31:0] high = 32'b01000010100011000000000000000000;

  wire c1_b;
  wire c1_s;

  fp_gt c1_b_c(.out(c1_b), .f1(low), .f2(RSI));

  fp_gt c1_s_c(.out(c1_s), .f1(RSI), .f2(high));

  always @ (*)
  begin
      if (c1_s)
      begin
          out1 = 1'b0;
          out2 = 1'b0;
      end
      else if (c1_b)
      begin
          out1 = 1'b1;
          out2 = 1'b0;
      end
      else
      begin
          out1 = 1'b0;
          out2 = 1'b1;
      end
  end
endmodule