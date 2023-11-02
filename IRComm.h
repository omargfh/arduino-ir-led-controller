#ifndef IRComm_H
#define IRComm_H
#include "IRSemantics.h"

typedef struct {
    uint8_t cmd;
    uint8_t repeat;
    uint8_t delay;
} IRCommand_t;

#ifdef __cplusplus
 extern "C" {
#endif

IRCommand_t deserializeCommand(uint16_t serial);
uint16_t serializeCommand(IRCommand_t cmd);

#ifdef __cplusplus
}
#endif

#endif
