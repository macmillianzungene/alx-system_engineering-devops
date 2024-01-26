#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    pid_t child_pid;
    int i;

    /* Create 5 zombie processes */
    for (i = 0; i < 5; i++) {
        child_pid = fork();

        /* In the child process */
        if (child_pid == 0) {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }

    /* Sleep for a while to ensure the child processes have finished */
    sleep(10);

    return 0;
}

