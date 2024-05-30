#![no_std]
#![no_main]

use panic_halt as _;

use core::ffi::c_char;

#[no_mangle]
pub extern "C" fn rustc_testr(left: c_char, right: c_char) -> c_char {
    left + right
}
