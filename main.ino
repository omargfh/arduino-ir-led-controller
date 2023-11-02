#include <Arduino.h>
#include "PinDefinitionsAndMore.h"
#include <IRremote.hpp>

#include "IRSemantics.h"
#include "IRComm.h"

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(115200);

  Serial.println(F("START IR LED Controller from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));
  Serial.print(F("Send IR signals at pin "));
  Serial.println(IR_SEND_PIN);
}

void loop() {
  if (Serial.available() != 4)
    return;

  byte bytes[4];
  unsigned long int result;
  Serial.readBytes(bytes, 4);
  for (int i = 0; i < 4; i++) {
    result |= (static_cast<unsigned long>(bytes[i]) << (8 * i));
  }

  IRCommand_t irCommand = deserializeCommand(result);

  Serial.print("Command: ");
  Serial.println(irCommand.cmd, HEX);

  IrSender.sendNEC(0xCF00, irCommand.cmd, 4);
  delay(50);
}
