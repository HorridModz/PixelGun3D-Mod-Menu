//(StackOverflow credit here)
#define __STDC_FORMAT_MACROS
#include <inttypes.h>

char* Offset2String(uint64_t offset) {
	char buf[256];
	snprintf(buf, sizeof(buf), "%" PRIu64, offset);
	return(buf);
}