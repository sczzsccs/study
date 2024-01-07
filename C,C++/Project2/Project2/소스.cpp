#include <stdio.h>

#define MLED_DATA		0x01
#define MLED_SHIFT		0x02
#define MLED_CLEAR		0x04
#define MLED_LATCH1	0x10
#define MLED_LATCH2	0x20

void matrix_led(int data)
{
	bool Bit[16];
	int tmp = ~data;
	int MLED_PORT = 0;
	MLED_PORT |= MLED_CLEAR;
	MLED_PORT &= ~(MLED_LATCH1 | MLED_LATCH2);

	for (int i = 0; i < 16; i++) {
		if (i % 4 == 0) { printf("\n"); }

		if (tmp & 0x8000) MLED_PORT |= MLED_DATA;
		else MLED_PORT &= ~MLED_DATA;
		printf("%d ", MLED_PORT & MLED_DATA);
		MLED_PORT |= MLED_SHIFT;
		tmp <<= 1;
		MLED_PORT &= ~MLED_SHIFT;
	}
	MLED_PORT |= (MLED_LATCH1 | MLED_LATCH2);
	MLED_PORT &= ~(MLED_LATCH1 | MLED_LATCH2);
}

void main() {
	unsigned int led_order[16] = {
	0x0001, 0x0002, 0x0004, 0x0008, 0x0080, 0x0800, 0x8000, 0x4000,
	0x0400, 0x0040, 0x0020, 0x0200, 0x2000, 0x1000, 0x0100, 0x0010
	};
	for (int  i = 0; i < sizeof(led_order)/sizeof(int); i++)
	{
		matrix_led(led_order[i]);
		printf_s("\n");
	}
}