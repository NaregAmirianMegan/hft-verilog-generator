# fpga-accel-htf
## Intro
Convert json descriptions of quant algorithms to verilog HDL and backtest the hardware on price time series data. 
## Usage
### Requirements 
- icarus verilog compiler
- gtkwave
- python 3.6 or greater <br>
### Summary
Given CSV data `src/generator/gen_testbench.py` generates a raw input hex file and a verilog test bench used to input the data signals to the fpga hardware. Given a json formatted description of a rule based quantitative algorithm `src/generator/gen_verilog.py` generates a verilog module describing the behavior in hardware. When compiled with iverilog the verilog test bench will generate an output file of buy/sell/hold signals over time which can be analyzed by `src/analysis/profit_analyzer.py` to discover statistics about the algorithm such as total percent profit and average percent profit per trade (buy, sell).
### File Formats
CSV Data: <br>
```
field1, field2, ...
data1, data2, ...
...
```
JSON Algo Description: <br>
```
{
}
```
### Example 1
Ex1
### Example 2
Ex2
## Sample Results
## Credits
