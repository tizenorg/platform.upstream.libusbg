check_PROGRAMS = test
test_SOURCES = test.c usbg-test.c usbg-io-wrappers.c
test_LDFLAGS = -ldl
test_LDFLAGS += $(CMOCKA_LIBS)
test_LDFLAGS += $(LIBCONFIG_LIBS)
test_LDADD = ./libusbg.so
test_CPPFLAGS = -I$(top_srcdir)/include/

./libusbg.so:
	-ln -s $(top_srcdir)/src/.libs/libusbg.so* .
CLEANFILES = libusbg.so*

check_SCRIPTS = ./test.sh
TESTS = $(check_SCRIPTS)
