#![no_std]
#![no_main]

use panic_halt as _;

use core::ffi::c_char;
use core::ffi::c_int;
use core::ffi::c_uchar;

#[no_mangle]
pub extern "C" fn rustc_testr(left: c_char, right: c_char) -> c_char {
    left + right
}

/// pub extern "C" fn rustc_edit_array(arr_ptr: *mut libc::c_uchar)
/// replace following unsigned char array with the empty byte.
#[no_mangle]
pub extern "C" fn rustc_edit_array(arr_ptr: *mut c_uchar, arr_len: c_int) {
    for i in 0..arr_len {
        let increc_ptr = arr_ptr.wrapping_add(i as usize);
        unsafe {
            *increc_ptr = 0x00;
        }
    }
}