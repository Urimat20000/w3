#include <stdio.h>
#include <math.h>



__inline double rand01_kiss(void)
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



/* Gaussian distribution with zero mean and unit variance
 * using the ratio method */
__inline double gaussrand_kiss(void)
{
  double x, y, u, v, q;
  do {
    u = 1 - rand01_kiss();
    v = 1.7156*(rand01_kiss() - .5);  /* >= 2*sqrt(2/e) */
    x = u - 0.449871;
    y = fabs(v) + 0.386595;
    q = x*x  + y*(0.196*y - 0.25472*x);
    if (q < 0.27597) break;
  } while (q > 0.27846 || v*v > -4*u*u*log(u));
  return v/u;
}


int main(void)
{
  int i;

  for ( i = 0; i < 100; i++ )
    printf("%f\n", rand01_kiss());
  return 0;
}