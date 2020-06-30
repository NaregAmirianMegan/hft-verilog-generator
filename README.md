# fpga-accel-htf
## Intro
A simple HLS tool that allows users to specify trading parameters and generates virtual hardware that speeds up and parallelizes the rule based algorithm. The generated hardware assumes single precision IEEE754 floating point numbers as inputs. 
## Usage
Requirements (MacOS): icarus verilog compiler, gtkwave, > python 3.6 <br>
Given csv data input the software generates a raw input file and verilog test bench used to input the data signals to the fpga hardware. Given a json formatted description of a rule based quantitative algorithm the software generates a verilog module describing the behavior in hardware. The verilog test bench will generate an output file of buy/sell/hold signals over time which can be analyzed by the software to discover statistics about the algorithm such as total percent profit and average percent profit per trade (buy, sell).
### Example 1
Ex1
### Example 2
Ex2
## Sample Results
## Credits
