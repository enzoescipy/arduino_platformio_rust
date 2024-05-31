#include "test_lib_cpp.h"
;
extern "C" char rustc_testr(char left, char right);

char test(char foo, char doo) {
  return rustc_testr(foo, doo);
}