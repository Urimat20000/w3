#include <stdio.h>

typedef unsigned char BYTE;

void ahtopb (char *ascii_hex, BYTE *p_binary, int bin_len)
{
	BYTE    nibble;
	int     i; 
	
	for ( i=0; i<bin_len; i++ ) {
        nibble = ascii_hex[i * 2];
	    if ( nibble > 'F' )
	        nibble -= 0x20;   
	    if ( nibble > '9' )
	        nibble -= 7;      
	    nibble -= '0';   
	    p_binary[i] = nibble << 4;
		
	    nibble = ascii_hex[i * 2 + 1];
	    if ( nibble > 'F' )
			nibble -= 0x20;
        if ( nibble > '9' )
            nibble -= 7;   
        nibble -= '0';
		p_binary[i] += nibble;
	}
}

int main(){
BYTE	p[64], q[64], s[64];
//printf("%d\n%d\n", &p, &q);
ahtopb("E65097BAEC92E70478CAF4ED0ED94E1C94B154466BFB9EC9BE37B2B0FF8526C222B76E0E915017535AE8B9207250257D0A0C87C0DACEF78E17D1EF9DC44FD91F", p, 64);
ahtopb("E029AEFCF8EA2C29D99CB53DD5FA9BC1D0176F5DF8D9110FD16EE21F32E37BA86FF42F00531AD5B8A43073182CC2E15F5C86E8DA059E346777C9A985F7D8A867", q, 64);
ahtopb("10d6333cfac8e30e808d2192f7c0439480da79db9bbca1667d73be9a677ed31311f3b830937763837cb7b1b1dc75f14eea417f84d9625628750de99e7ef1e976", s, 64);
printf("%d\n%d\n", *p, *q);
}