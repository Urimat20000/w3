#include <stdio.h>
static unsigned jsr = 7;
#define SHR3(jsr) (jsr = jsr + 5)

double rand01_kiss(void)
{
#define znew(z)   (z = 36969 * (z & 65535) + (z >> 16))
#define wnew(w)   (w = 18000 * (w & 65535) + (w >> 16))
#define MWC(z, w) ((znew(z) << 16) + wnew(w))
#define SHR3(jsr) (jsr ^= (jsr << 17), jsr ^= (jsr >> 13), jsr ^= (jsr << 5))
#define CONG(jc)  (jc = 69069 * jc + 1234567)
#define KISS(z, w, jc, jsr) ((MWC(z, w) ^ CONG(jc)) + SHR3(jsr))
  static unsigned z = 1234567, w = 2345678, jsr = 3456789, jcong = 4567890;
  return KISS(z, w, jcong, jsr) / 4294967296.0;
}

int main(void){
	printf("%d\n", SHR3(jsr));
	printf("%d\n", SHR3(jsr));
	printf("%d\n", 1234567 >> 16);
	printf("%f\n", rand01_kiss());
	printf("%f\n", rand01_kiss());
	#define znew(z)   (z = 36969 * (z & 65535) + (z >> 16))
	static unsigned z = 1234567;
	printf("%u\n", znew(z) << 16);
	printf("%d\n", z);
}