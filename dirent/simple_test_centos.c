#include <stdio.h>
#include <dirent.h>
#include <syscall.h>

#define NVME_CLASS_PATH "/work1/obordes/test/dirent/test"
#define MAX_DISKS 5
#define MAX_NAME_LEN 80
#define MAX_PATH_LEN 256
#define MAX_NS_PER_DISK 32

#define nvmeof_out printf 

int nb_disk = 0;
int ns[MAX_DISKS][MAX_NS_PER_DISK];

void test_dents(int fd)
{
	char buf[512];
	int v= syscall (__NR_getdents, fd, buf, 512);
	printf ("getdents return: buf=%s\n", buf);
}

int scan_nvme_disk(char * nvme_path)
{
	struct dirent *entry;
	DIR * d = opendir(nvme_path);
	char buf[80];

	if (!d) {
		nvmeof_out ("cannot open dir %s\n", nvme_path);
		return -1;
	}

	nvmeof_out ("opening dir %s\n", nvme_path);
	test_dents ((int) (d-> d_ino));

#if 0
	while ((entry= readdir(d)))
	{
		if (entry->d_name[0] != '.') {
			nvmeof_out ("nvme disk entry: %s\n", entry->d_name);
			sprintf (buf, "%s/%s", nvme_path, entry->d_name);
			scan_nvme_ns(nb_disk, buf); 
			nb_disk++;
		}
	}
#endif
	closedir(d);
	return 0;

}


int scan_nvme_ns(int disk, char * disk_path)
{
	DIR *d;
	struct dirent *entry;
	int i=0;
	int nb_ns = 0;

	d = opendir(disk_path);
	if (!d) {
		nvmeof_out ("cannot open dir %s\n", disk_path);
		return -1;
	}
	while ((entry= readdir(d))) 
	{
		if (entry->d_name[0] != '.') {
			nvmeof_out ("nvme namespace entry: %s\n", entry->d_name);
			//ns[disk][i] = malloc (), "%s", entry->d_name);
			//sprintf (ns[disk][nb_disk++], "%s", entry->d_name);
			nb_ns++;
		}
	}
	nvmeof_out ("Nombre de namespace= %d\n", nb_ns);
	return 0;
}

int main()
{
	DIR *d;
	int v;
	int i;
	char nvme_path[MAX_PATH_LEN];
	char disk_name[MAX_NAME_LEN];

	nvmeof_out ("starting simple_test\n");
	sprintf (nvme_path, "%s", NVME_CLASS_PATH);
	scan_nvme_disk(nvme_path);

#if 0
	for (i=0; i < nb_disk; i++)
	{
		sprintf (disk_name, NVME_CLASS_PATH "%d",i);
		scan_nvme_ns (i, disk_name); 
	}
#endif
	//scan_nvme_ns(d);
}
