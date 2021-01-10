"""Reverse of a given number.

Algo
----

00. Start
01. Read a number n
02. rev = 0
03. i = n
04. rem = i%10 This gives the last digit in the number
05. rev = rev * 10 + rem
06. i = i // 10 This gives the rest of the number without the last digit
07. if i > 0 go to step 04
08. Print rev
09. Stop


n       i       rem     rev
1234                    0
        1234    4       0*10 + 4 = 4
        123     3       4*10 + 3 = 43
        12      2       43*10 + 2 = 432
        1       1       432*10 + 1 = 4321
        0


10) 1 (0
    0
   ---
    1

1 % 10 = 1
1 // 10 = 0


For loop in C based programming languages

for(int i=0; i <10; i = i+1){
    ...
    ...
}

for(Starting; condition; incrementing){

}

for(;0 == 0;) -> Infinite for loop
"""


def get_reverse(n):
    """Get reverse of a number."""
    rev = 0
    i = n
    while i > 0:
        rem = i % 10
        rev = rev * 10 + rem
        i = i // 10

    return rev


def test_get_reverse():
    """Test get reverse of a number."""
    assert get_reverse(1234) == 4321
    assert get_reverse(3445) == 5443
