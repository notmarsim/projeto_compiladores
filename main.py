import interpreter
import analyzer
import generator

analyzer.run(open("test.ft").read())
generator.run(open("test.ft").read())
interpreter.run(open("test.ft").read())
