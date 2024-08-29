#include <stdio.h>
#include <sys/dirent.h>
#include <mppa_async.h>
#include <sys/syscall.h>
#include "syscall_async.h"


#define NVME_CLASS_PATH "/sys/class/nvme"
#define MAX_DISKS 5
#define MAX_NAME_LEN 80
#define MAX_PATH_LEN 256
#define MAX_NS_PER_DISK 32


int nb_disk;
int ns[MAX_DISKS][MAX_NS_PER_DISK];

int
mppa_remote_client_send_request(syscall_arg_t *arg)
{
	mppa_rpc_request_t *req = &arg->rpc_req;
	const int current_cmd = req->cmd;

	if (current_cmd == __NR_write) 
		return -1;
	return -1;
	//printf("got a syscall number: %d\n", current_cmd);
}

int scan_nvme_disk(char * nvme_path)
{
	struct dirent *entry;
	DIR * d = opendir(nvme_path);
	printf ("opening dir \n");
	entry= readdir(d);
	while (entry) 
	{
		printf ("nvme disk entry: %s\n", entry->d_name);
		//sprintf (disk[nb_disk++], "%s", entry->d_name);
		nb_disk++;
	}
	closedir(d);

}

int test_dents(int fd)
{
	char buf[512];
	int v= syscall (_NR_getdents, fd, buf, 512);
	printf ("getdents return: buf=%s\n", buf);

}

int scan_nvme_ns(int disk, char * disk_path)
{
	DIR *d;
	struct dirent *entry;
	int i=0;

	d = opendir(disk_path);
#if 0
	while (entry= readdir(d)) 
	{
		printf ("nvme namespace entry: %s\n", entry->d_name);
		//ns[disk][i] = malloc (), "%s", entry->d_name);
		//sprintf (ns[disk][nb_disk++], "%s", entry->d_name);
	}
#else
	test_dents(d->d_ino);
#endif
}


int main()
{
	DIR *d;
	int v;
	int i;
	char nvme_path[MAX_PATH_LEN];
	char disk_name[MAX_NAME_LEN];

	printf ("starting simple_test\n");
	sprintf (nvme_path, "%s", NVME_CLASS_PATH);
	scan_nvme_disk(nvme_path);

	for (i=0; i < nb_disk; i++)
	{
		sprintf (disk_name, NVME_CLASS_PATH "%d",i);
		scan_nvme_ns (i, disk_name); 
	}
	//scan_nvme_ns(d);
}
