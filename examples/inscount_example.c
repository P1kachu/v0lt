#include <string.h>
#include <stdio.h>

// gcc -O0 examples/inscount_example.c -o examples/inscount_example.elf

int get_char(int x, int upper)
{
        char set[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        int ret = 0;
        ret += set[x];
        ret += upper;

        // Simulate Crackme doing lots of stuff
        for (int i = 0; i < 2500; ++i)
                x *= 2;

        return ret;
}

int main(int argc, char **argv)
{
        if (argc < 2)
                return -1;

        if (strlen(argv[1]) >= 22)
        {

                int i = 0;

                if (argv[1][i++] != get_char(8, 0))
                        return -1;
                if (argv[1][i++] != get_char(13, 32))
                        return -1;
                if (argv[1][i++] != get_char(18, 0))
                        return -1;
                if (argv[1][i++] != get_char(33, 0))
                        return -1;
                if (argv[1][i++] != get_char(17, 32))
                        return -1;
                if (argv[1][i++] != get_char(20, 32))
                        return -1;
                if (argv[1][i++] != get_char(2, 32))
                        return -1;
                if (argv[1][i++] != get_char(19, 32))
                        return -1;
                if (argv[1][i++] != get_char(8, 0))
                        return -1;
                if (argv[1][i++] != get_char(26, 0))
                        return -1;
                if (argv[1][i++] != get_char(13, 32))
                        return -1;
                if (argv[1][i++] != get_char(2, 0))
                        return -1;
                if (argv[1][i++] != get_char(14, 32))
                        return -1;
                if (argv[1][i++] != get_char(20, 32))
                        return -1;
                if (argv[1][i++] != get_char(13, 32))
                        return -1;
                if (argv[1][i++] != get_char(19, 0))
                        return -1;
                if (argv[1][i++] != get_char(8, 32))
                        return -1;
                if (argv[1][i++] != get_char(13, 0))
                        return -1;
                if (argv[1][i++] != get_char(32, 0))
                        return -1;
                if (argv[1][i++] != get_char(17, 0))
                        return -1;
                if (argv[1][i++] != get_char(20, 32))
                        return -1;
                if (argv[1][i++] != get_char(11, 32))
                        return -1;
                if (argv[1][i++] != get_char(25, 32))
                        return -1;

                printf("Congrats!\n");
                printf("The flag is %s\n", argv[1]);

                return 0;
        }

        return -2;
}
