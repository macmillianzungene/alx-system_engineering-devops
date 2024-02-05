#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit 1
end

# Get the input string
input_string = ARGV[0]

# Create a regular expression that matches "School"
regex = /School/

# Use the match method to find matches in the input string
matches = input_string.scan(regex)

# Print the matches
puts matches.join

