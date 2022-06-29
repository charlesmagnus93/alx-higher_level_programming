#!/usr/bin/python3
for a in range(97, 123)[::-1]:
    print(
        ('{}'.format(chr(a)) if a % 2 == 0 else '{}'.format(chr(a - 32))),
        end=''
    )
