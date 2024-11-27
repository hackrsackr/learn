const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, {s}!\n", . {"World"});
}

// run with zig run hello_world.zig