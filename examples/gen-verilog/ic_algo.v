`include "../../fpu/fp_gt.v"

module ic_algo(output out1, output out2, input [31:0] PRICE, input [31:0] SSA, input [31:0] SSB, input [31:0] KS, input [31:0] TS);
  reg out1 = 1'b0;
  reg out2 = 1'b1;
  reg [31:0] low = 32'b01000001111100000000000000000000;
  reg [31:0] high = 32'b01000010100011000000000000000000;

  wire c1_b;
  wire c2_b;
  wire c3_b;
  wire c4_b;
  wire c5_b;
  wire c1_s;
  wire c2_s;
  wire c3_s;
  wire c4_s;
  wire c5_s;

  fp_gt c1_b_c(.out(c1_b), .f1(SSA), .f2(PRICE));
  fp_gt c2_b_c(.out(c2_b), .f1(SSB), .f2(PRICE));
  fp_gt c3_b_c(.out(c3_b), .f1(SSA), .f2(SSB));
  fp_gt c4_b_c(.out(c4_b), .f1(PRICE), .f2(KS));
  fp_gt c5_b_c(.out(c5_b), .f1(TS), .f2(KS));

  fp_gt c1_s_c(.out(c1_s), .f1(SSA), .f2(PRICE));
  fp_gt c2_s_c(.out(c2_s), .f1(SSB), .f2(PRICE));
  fp_gt c3_s_c(.out(c3_s), .f1(SSB), .f2(SSA));
  fp_gt c4_s_c(.out(c4_s), .f1(KS), .f2(PRICE));
  fp_gt c5_s_c(.out(c5_s), .f1(KS), .f2(TS));

  always @ (*)
  begin
      if ((c1_s&c2_s)|c3_s|c4_s|c5_s)
      begin
          out1 = 1'b0;
          out2 = 1'b0;
      end
      else if (!(c1_b|c2_b)|c3_b|c4_b|c5_b)
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