#!/bin/bash

# Run test with io functions ovverride

LD_LIBRARY_PATH=. LD_PRELOAD=./usbg-io-wrappers.so ./test

