#include <stdio.h>
#include "IRSemantics.h"
#include "IRComm.h"

IRCommand_t deserializeCommand(uint16_t serial) {
    IRCommand_t cmd;
    cmd.cmd = (uint8_t) (serial >> 8);
    cmd.repeat = (uint8_t) (serial >> 4);
    cmd.delay = (uint8_t) serial;
    return cmd;
}

uint16_t serializeCommand(IRCommand_t cmd) {
    uint16_t serial = 0;
    serial |= (uint16_t) ((cmd.cmd << 8) & 0xFF00);
    serial |= (uint16_t) ((cmd.repeat << 4) & 0xF0);
    serial |= (uint16_t) (cmd.delay & 0xF);
    return serial;
}
