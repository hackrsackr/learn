# Assembling and Linking

nasm -f elf64 -g -F DWARF hello_world.asm
ld -e start -o hello_world hello_world.o
./hello_world
