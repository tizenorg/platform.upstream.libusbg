all: test.c usbg-test usbg-io-wrappers libusbg
	gcc -Wall -g test.c usbg-test -lcmocka $(shell pkg-config --libs --cflags libconfig) ./libusbg.so ./usbg-io-wrappers.so -I ../include -o test

usbg-test: usbg-test.h usbg-test.c
	gcc -g -c -I./ usbg-test.c -I ../include -o usbg-test

usbg-io-wrappers: usbg-io-wrappers.c
	gcc -Wall -fPIC -shared usbg-io-wrappers.c -lcmocka -Wl,--no-as-needed -ldl -o usbg-io-wrappers.so

libusbg:
	ln -s ../src/.libs/libusbg.so* .

