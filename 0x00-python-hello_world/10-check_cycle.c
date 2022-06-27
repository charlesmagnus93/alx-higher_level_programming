#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checker
 * @list: pointer to head of list
 * Return: number
 */
int check_cycle(listint_t *list) {
    struct listint_s *one, *two;
    one = two = list;

    while(one && two && two->next)
    {
        one = one->next;
        two = two->next->next;
        if (one == two)
            return 1;
    }
    return 0;
}
