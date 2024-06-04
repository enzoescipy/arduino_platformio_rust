#include <Arduino.h>
#include <test_lib_cpp.h>

;
extern "C" char rustc_testr(char left, char right);
extern "C" void rustc_edit_array(unsigned char * arr_ptr, int arr_len);

void setup()
{
  Serial.begin(9600);
  Serial.println((int) rustc_testr(1,2)); // this is the testcode for rust-compiled statical lib. comment this line when production.
  Serial.println((int) test(3,4));
  int len = 5;
  unsigned char * test_byte_arr_ptr = (unsigned char *) malloc(sizeof(char) * len);
  rustc_edit_array(test_byte_arr_ptr, len);
  for (int i = 0; i < 15; i++) {
    Serial.println(test_byte_arr_ptr[i]);
  }
}

void loop()
{

}
