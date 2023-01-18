#!/usr/bin/env python3
import atheris
import io
import sys
import logging

with atheris.instrument_imports():
    import autoflake

logging.disable(logging.ERROR)


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    source = fdp.ConsumeUnicodeNoSurrogates(fdp.remaining_bytes())
    autoflake.check(source)
    autoflake.fix_code(source)


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == '__main__':
    main()
