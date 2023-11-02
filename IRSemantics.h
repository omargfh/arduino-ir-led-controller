#pragma once
#ifndef IRSemantic_H
#define IRSemantic_H

#include <stdint.h>
#define PROTOCOL "NEC"

enum REMOTE_COMMAND {
    ADDR = 0xCF00,
    BRIGHTNESS_UP = 0x5C,
    BRIGHTNESS_DOWN = 0x5D,
    PLAY = 0x41,
    POWER = 0x40,
    COLOR_RED = 0x58,
    COLOR_GREEN = 0x59,
    COLOR_BLUE = 0x45,
    COLOR_RED1 = 0x54,
    COLOR_ORANGE = 0x54,
    COLOR_GREEN1 = 0x55,
    COLOR_BLUE1 = 0x59,
    COLOR_CYAN = 0x59,
    COLOR_RED2 = 0x50,
    COLOR_GREEN2 = 0x51,
    COLOR_BLUE2 = 0x4D,
    COLOR_RED3 = 0x1C,
    COLOR_GREEN3 = 0x1D,
    COLOR_PINK = 0x1E,
    COLOR_BLUE3 = 0x1E,
    COLOR_RED4 = 0x18,
    COLOR_YELLOW = 0x18,
    COLOR_GREEN4 = 0x19,
    COLOR_BLUE4 = 0x1A,
    COLOR_PURPLE = 0x1A,
    COLOR_WHITE = 0x44,
    MUSIC1 = 0x48,
    MUSIC2 = 0x4C,
    MUSIC3 = 0x1F,
    MUSIC4 = 0x5B,
    AUTO = 0x17,
    SLOW = 0x13,
    QUICK = 0xF,
    FLASH = 0xB,
    JUMP3 = 0x4,
    JUMP7 = 0x5,
    FADE3 = 0x6,
    FADE7 = 0x7,
    RED_UP = 0x14,
    RED_DOWN = 0x10,
    GREEN_UP = 0x15,
    GREEN_DOWN = 0x11,
    BLUE_UP = 0x16,
    BLUE_DOWN = 0x12,
    DIY1 = 0xC,
    DIY2 = 0xD,
    DIY3 = 0xE,
    DIY4 = 0x8,
    DIY5 = 0x9,
    DIY6 = 0xA
};

#endif
