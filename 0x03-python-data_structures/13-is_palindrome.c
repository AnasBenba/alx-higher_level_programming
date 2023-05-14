#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 1 if list is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	listint_t *ptr1 = *head;
	int len = 1, value1 = 0, value2 = 0;

	if (*head == NULL)
	{
		return (1);
	}
	while (ptr1->next != NULL)
	{
		ptr1 = ptr1->next;
		len++;
	}
	if (len % 2 != 0)
	{
		int i = 1;

		while (i <= len / 2)
		{
			value1 += ptr->n;
			ptr = ptr->next;
			i++;
		}
		i++;
		ptr = ptr->next;
		while (i <= len)
		{
			value2 += ptr->n;
			ptr = ptr->next;
			i++;
		}
	}
	else
	{
		int i = 1;

		while (i <= len / 2)
		{
			value1 += ptr->n;
			ptr = ptr->next;
			i++;
		}
		while (i <= len)
		{
			value2 += ptr->n;
			ptr = ptr->next;
			i++;
		}
	}
	if (value1 == value2)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
