1.  you must compile this library with this command : 
    `cargo +nightly build -Z build-std=core --target=avr-unknown-gnu-atmega328 --release`

2.  write down the function's header to the src/rust_test_sample.h.

3.  place the avr-unknown-gnu-atmega328/release/librust_test_sample.a to the proper lib folder.
    in platform.io, proper folder is /lib .

4.  place the src/rust_test_sample.h to the proper includes folder.
    in platform.io, proper folder is /include .
