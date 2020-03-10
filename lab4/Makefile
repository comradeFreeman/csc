CMP=as
LNR=ld
ASFLAGS=-g -c
ASFLAGSDBG=--gdwarf2
LNRFLAGS=-static
SRCS=$(wildcard *.s)
OBJS=$(SRCS:.s=.o)
PROGS=$(OBJS:.o=)

.PHONY: all clean
.SILENT: clean

exit: exit.s
	$(CMP) $(ASFLAGS) -o $($<:.s=.o) -c $<
	$(LNR) $(LNRFLAGS) -o $@ $($<:.s=.o)
dbg4: 4.s
	$(CMP) $(ASFLAGSDBG) -o 4.o -c $<
	$(LNR) $(LNRFLAGS) -o $@ 4.o

all: $(PROGS) $(OBJS)

$(PROGS): %: %.o
	$(LNR) $(LNRFLAGS) -o $@ $<
$(OBJS): %.o: %.s
	$(CMP) $(ASFLAGS) -o $@ -c $<

clean:
	rm -rf *.o
	ls | grep -v '\.\|Makefile' | xargs rm -rf
