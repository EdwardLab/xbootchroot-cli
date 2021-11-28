#xbootchroot by xingyujie GPL 3.0 LICENSE

import getopt

import os

import sys

opts,args = getopt.getopt(sys.argv[1:],'-h-r:-v',['help','rootfs=','version'])

for opt_name,opt_value in opts:

    if opt_name in ('-h','--help'):

        print("Usage: xbootchroot [OPTION]... [COMMAND ...")

        print("""

OPTIONs:

  -h, --help                      displays this help message

  -r, --rootfs [rootfsdir].         Specify rootfs path

  -m, --machine                   displays machine parseable output

  -s, --script                    never prompts for user intervention

  -v, --version                   displays the version

  -a, --align=[none|cyl|min|opt]  alignment for new partitions

        """)

        exit()

    if opt_name in ('-v','--version'):

        print("""

xbootchroot (GNU xbootchroot) 1.1

By: xingyujie

Github: https://github.com/xingyujie

        

        

        """)

        exit()

    if opt_name in ('-r','--rootfs'):

        rootfs = opt_value

        os.system("""

unset TMP TEMP TMPDIR LD_PRELOAD LD_DEBUG

path="${PATH}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

#hostname FlyGeekPro

mount -t proc proc ./rootfs/proc

mount -o bind /sdcard ./rootfs/sdcard

mount -o bind /sys ./rootfs/sys

mount -o bind /dev ./rootfs/dev

mount -o bind /system ./rootfs/system

mount -o bind /data ./rootfs/data

chroot """ + """rootfs """ + """/bin/login

""")

        # do something

        exit()
