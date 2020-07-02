`include "fp_gt.v"

module rsi(output out1, output out2, input [31:0] RSI);

    reg out1 = 1'b1;
    reg out2 = 1'b0;

    reg [31:0] low = 32'b01000001111100000000000000000000;
    reg [31:0] high = 32'b01000010100011000000000000000000;

    wire h, l;

    fp_gt higher(.out(h), .f1(RSI), .f2(high));
    fp_gt lower(.out(l), .f1(low), .f2(RSI));

    always @ (*)
    begin
        if (h) // sell logic
        begin
            out1 = 1'b0;
            out2 = 1'b0;
        end
        else if (l) // buy logic
        begin
            out1 = 1'b0;
            out2 = 1'b1;
        end
        else 
        begin
            out1 = 1'b1;
            out2 = 1'b0;
        end
    end
endmodule