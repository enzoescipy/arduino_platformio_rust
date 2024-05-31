#include <Arduino.h>
#include <test_lib_cpp.h>

;
extern "C" char rustc_testr(char left, char right);

void setup()
{
  Serial.begin(9600);
  Serial.println((int) rustc_testr(1,2)); // this is the testcode for rust-compiled statical lib. comment this line when production.
  Serial.println((int) test(3,4));
}

void loop()
{

}
