#!/usr/bin/perl

# Template to write to a file

# file we want to write to
my $file = "";

# attempt to open the file
open (my $fh, '>', $file) or die $!;

# write content to file
print $fh "Text written to file\n";

# close the file
close $fh;
