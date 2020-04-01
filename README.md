# py-four

**py-four** is a Python interpreter for the [**4** esoteric programming language](http://esolangs.org/wiki/4). You can try it in your browser on [Try it Online!](https://tio.run/##HYuJCcBAEAI7CrP/pf/CNl5EZBTM3XgasMaIxk0R4U2GqDKbHtU5A4fB4RXo4gI3yVFwXXTxlvFbtYoo5rL5HTlF5u4H) thanks to [@DennisMitchell](https://github.com/DennisMitchell/).

For a *quick* introduction with **4** code, scroll to the [**4 Guide**](https://github.com/urielieli/py-four/#4-guide).

The `four` directory is a package for the interpreter; The `samples` directory contains **4** code samples.

## Quickstart

To use the interpreter, either pass a file name or the raw code through the `-e` option:

```
$ python four samples/hello.4
Hello World!

$ python four -e 3.60072601735005014
HI
```

The **transpiled python source** can be viewed with the `-v | --verbose` option.

~Optimizations are available under the `-o | --optimize` option~ (currently unstable).

## 4 Guide

**4** is a simple language with a small instruction set, created by [Vriskanon](https://esolangs.org/wiki/User:Vriskanon).
This guide contains a brief summary of the [esolangs page](http://esolangs.org/wiki/4) documentation.

Every program starts with `3.` and ends with `4`, and uses a **memory area with 100 numeric cells**, numbered `00`-`99`.

The code consists of several instructions, starting with an **1-byte opcode**, followed by [0 to 3] **2-bytes operands**.

### Operations

*In the following examples `G[x]` denotes the array cell at `x`*.

*Also, **4** code should not contain ant non-numeric characters. Spaces and brackets here are for demonstration.*.

**Assignment:** **set** (opcode `6`) performs `G[operand 1] = operand 2`, so `6 00 01` will set `G[0]` value to `1`.

**Math:** **add** (opcode `0`), **subtract** (opcode `1`), **multiply** (opcode `2`), and **floor divide** (opcode `3`), each has three operands, and performs `G[operand 1] = operation(G[operand 2], G[operand 3])`, so `2 00 01 02` will multiply `G[1]` and `G[2]` into `G[0]`.

**IO:** **input** (opcode `7`) and **output** (opcode `5`) each read a byte into or write a byte from `G[operand 1]`, so `5 00` outputs `G[0]` in unicode.

**Branching:** **begin loop** (opcode `8`) and **end loop** (opcode `9`) instructions execute all the instructions between them until the counter at `G[operand 1]` is `0`,
so `8 01 [7 00] 9` (without brackets) will input a byte into `G[0]` until `G[1]` is zero (possibly never).

**exit** (opcode `4`) exits the program.

### Example

The program `3.70080050070094` outputs a string received as input. Lets break it down:

```
3.     |
7 00   | input a byte into G[0]
8 00   | while grid[0] is not null
  5 00 |     output G[0] as a byte
  7 00 |     input a byte into G[0]
9      | close loop
4      |
```