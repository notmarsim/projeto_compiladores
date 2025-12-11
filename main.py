from interpreter import run
import analyzer
import generator

analyzer.run(open("test.ft").read())

run(open("test.ft").read())

generator.run(open("test.ft").read())
