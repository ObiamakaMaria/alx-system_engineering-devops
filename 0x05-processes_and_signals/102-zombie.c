#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - This function creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	char counter = 0;
	pid_t pid;

	while (counter < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			counter++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}

/**
 * infinite_while - Thus function runs an infinite while loop.
 *
 * Return: Returns 0 on sucess.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
