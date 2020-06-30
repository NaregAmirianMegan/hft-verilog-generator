// Using IEEE-754 Single Precision Float

/*
    fp_gt: listens to two 32 bit inputs which should represent 2 floating point
    precision numbers. It sets out if f1 > f2, else it zeros out.

    This is the main driver for looking at the technical indicators. Under IEEE-754
    we can compare the binary representation the same as we would for normal integers.
*/
module fp_gt (output out, input [31:0] f1, input [31:0] f2);

    reg out = 1'b0;

    always @ (*)
    begin 
        if (f1[31] == 1 && f2[31] == 1)
        begin 
            if (f1[30:0] > f2[30:0])
            begin
                out = 1'b0;
            end
            else
            begin
                out = 1'b1;
            end
        end
        else if (f1[31] == 0 && f2[31] == 0)
        begin
            if (f1[30:0] > f2[30:0])
            begin
                out = 1'b1;
            end
            else
            begin
                out = 1'b0;
            end
        end
        else
        begin
            if (f1[31] == 1)
            begin
                out = 1'b0;
            end
            else
            begin
                out = 1'b1;
            end
        end
    end
endmodule