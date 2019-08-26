# py-four

This is a python implementation to the [4 esoteric programming language](http://esolangs.org/wiki/4).

To use the interpreter, provide a name of a file containing the source code, or use the `-e` option to provide code through the command line.

You can try py-four in your browser on [Try it Online!](https://tio.run/##HYuJCcBAEAI7CrP/pf/CNl5EZBTM3XgasMaIxk0R4U2GqDKbHtU5A4fB4RXo4gI3yVFwXXTxlvFbtYoo5rL5HTlF5u4H) thanks to [@DennisMitchell](https://github.com/DennisMitchell/).

## Optimizations

Transpilation optimizations are available under the `-o` `--optimize` option.

They are currently limited to constants reduction.

## Verbose mode

The transpiled source can be viewed with the `-v` `--verbose` option.