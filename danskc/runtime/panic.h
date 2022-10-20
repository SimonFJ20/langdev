#ifndef PANIC_H
#define PANIC_H

#include <stdio.h>

#define PANIC(msg) (printf("panic: \"%s\", at ./%s:%d in \"%s\"", msg, __FILE__, __LINE__, __FUNCTION__))

#endif