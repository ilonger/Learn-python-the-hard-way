# -*- coding: utf-8 -*-
__author__ = 'Liu'

print("现在开始练习一些东西")
print("You \'d need to know\'bout escapes with \\ that do \n new lines and \t tabs")
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion for intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print("This is should be five:%s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With the start point of %d" % start_point)
print("We have %d beans,%d jars,%d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way")
print("We have %d beans,%d jars,%d crates." % secret_formula(start_point))